import json
from pathlib import Path

import streamlit as st
import tensorflow as tf

from config import CLASS_NAMES_PATH, MODEL_PATH


@st.cache_resource(show_spinner="Memuat model prediksi...")
def load_prediction_model():
    model_path = Path(MODEL_PATH)
    if not model_path.exists():
        raise FileNotFoundError(
            f"Model tidak ditemukan di: {model_path}. "
            "Masukkan file efficientnetb0_direct_multiclass.keras ke folder models/."
        )
    return tf.keras.models.load_model(model_path)


@st.cache_data
def load_class_names():
    class_path = Path(CLASS_NAMES_PATH)
    if not class_path.exists():
        raise FileNotFoundError(f"class_names.json tidak ditemukan di: {class_path}")

    with open(class_path, "r", encoding="utf-8") as file:
        return json.load(file)
