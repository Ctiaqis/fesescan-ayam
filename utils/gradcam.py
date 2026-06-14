import cv2
import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow.keras.applications.efficientnet import preprocess_input

from config import IMG_SIZE


def find_last_conv_layer(model):
    """Mencari layer convolution terakhir secara rekursif."""
    candidates = []

    def collect_layers(current_model):
        for layer in current_model.layers:
            if isinstance(layer, tf.keras.Model):
                collect_layers(layer)
            else:
                try:
                    if len(layer.output.shape) == 4:
                        candidates.append(layer)
                except Exception:
                    pass

    collect_layers(model)

    if not candidates:
        raise ValueError("Layer convolution 4D tidak ditemukan untuk Grad-CAM.")

    return candidates[-1].name


def make_gradcam_heatmap(image: Image.Image, model, pred_index=None):
    """Membuat heatmap Grad-CAM.

    Fungsi ini dibuat defensif. Jika struktur graph model tidak kompatibel,
    pemanggil sebaiknya menangkap error dan tetap menampilkan prediksi utama.
    """
    img = image.convert("RGB").resize(IMG_SIZE)
    img_array = np.array(img).astype(np.float32)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    last_conv_layer_name = find_last_conv_layer(model)
    last_conv_layer = model.get_layer(last_conv_layer_name)

    grad_model = tf.keras.models.Model(
        inputs=model.inputs,
        outputs=[last_conv_layer.output, model.output]
    )

    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img_array)
        if pred_index is None:
            pred_index = tf.argmax(predictions[0])
        class_channel = predictions[:, pred_index]

    grads = tape.gradient(class_channel, conv_outputs)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

    conv_outputs = conv_outputs[0]
    heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)

    heatmap = tf.maximum(heatmap, 0) / (tf.reduce_max(heatmap) + 1e-8)
    return heatmap.numpy()


def create_gradcam_overlay(image: Image.Image, model, alpha=0.45):
    original = image.convert("RGB")
    original_arr = np.array(original)

    heatmap = make_gradcam_heatmap(original, model)
    heatmap = cv2.resize(heatmap, (original_arr.shape[1], original_arr.shape[0]))
    heatmap_uint8 = np.uint8(255 * heatmap)
    heatmap_color = cv2.applyColorMap(heatmap_uint8, cv2.COLORMAP_JET)
    heatmap_color = cv2.cvtColor(heatmap_color, cv2.COLOR_BGR2RGB)

    overlay = np.uint8((1 - alpha) * original_arr + alpha * heatmap_color)
    return overlay
