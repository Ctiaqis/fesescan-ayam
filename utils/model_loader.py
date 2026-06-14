import json
from pathlib import Path

import keras
import streamlit as st
import tensorflow as tf

from config import CLASS_NAMES_PATH, MODEL_PATH


def _patch_quantization_config_compat():
    """Buang argumen 'quantization_config' yang tidak dikenal oleh Keras versi ini.

    Model disimpan dengan Keras yang lebih baru yang menambahkan kunci
    'quantization_config' ke konfigurasi setiap layer. Pada model float32 biasa
    nilainya None (tanpa kuantisasi), sehingga aman untuk diabaikan saat memuat.
    """
    if getattr(keras.layers.Layer, "_quantization_config_patched", False):
        return

    original_init = keras.layers.Layer.__init__

    def patched_init(self, *args, **kwargs):
        kwargs.pop("quantization_config", None)
        original_init(self, *args, **kwargs)

    patched_init._quantization_config_patched = True
    keras.layers.Layer.__init__ = patched_init
    keras.layers.Layer._quantization_config_patched = True


@st.cache_resource(show_spinner="Memuat model prediksi...")
def load_prediction_model():
    model_path = Path(MODEL_PATH)
    if not model_path.exists():
        raise FileNotFoundError(
            f"Model tidak ditemukan di: {model_path}. "
            "Masukkan file efficientnetb0_direct_multiclass.keras ke folder models/."
        )
    _patch_quantization_config_compat()
    return tf.keras.models.load_model(model_path)


@st.cache_data
def load_class_names():
    class_path = Path(CLASS_NAMES_PATH)
    if not class_path.exists():
        raise FileNotFoundError(f"class_names.json tidak ditemukan di: {class_path}")

    with open(class_path, "r", encoding="utf-8") as file:
        return json.load(file)
