import cv2
import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow.keras.applications.efficientnet import preprocess_input

from config import IMG_SIZE


def find_feature_layer(model):
    """Cari layer level-atas terakhir yang menghasilkan feature map 4D.

    Pada model dengan backbone bersarang (mis. EfficientNetB0 dipakai sebagai
    submodel), layer ini adalah submodel itu sendiri — output-nya berupa feature
    map (H, W, C) yang ideal untuk Grad-CAM. Mengambil layer di level atas
    menghindari error 'graph disconnected' saat membangun grad model di Keras 3,
    yang terjadi bila kita mencoba mengakses layer yang tersembunyi di dalam
    submodel.
    """
    for layer in reversed(model.layers):
        try:
            shape = layer.output.shape
        except Exception:
            continue
        if len(shape) == 4:
            return layer
    raise ValueError("Layer feature map 4D tidak ditemukan untuk Grad-CAM.")


def make_gradcam_heatmap(image: Image.Image, model, pred_index=None):
    """Membuat heatmap Grad-CAM dari feature map konvolusi terakhir.

    Menangani dua bentuk arsitektur:
    - Backbone bersarang (EfficientNetB0 sebagai submodel): submodel dijalankan
      langsung untuk mendapatkan feature map, lalu layer di atasnya
      (GlobalAveragePooling → Dropout → Dense) diterapkan manual. Ini perlu
      karena Keras 3 tidak dapat membangun ulang model fungsional dari output
      layer yang berada di dalam submodel.
    - Model datar: feature map dan prediksi diambil lewat satu grad model biasa.
    """
    img = image.convert("RGB").resize(IMG_SIZE)
    img_array = np.array(img).astype(np.float32)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    img_tensor = tf.convert_to_tensor(img_array)

    feature_layer = find_feature_layer(model)

    if isinstance(feature_layer, tf.keras.Model):
        # Backbone bersarang → forward manual.
        feature_index = model.layers.index(feature_layer)
        top_layers = model.layers[feature_index + 1:]

        with tf.GradientTape() as tape:
            conv_outputs = feature_layer(img_tensor, training=False)
            tape.watch(conv_outputs)
            x = conv_outputs
            for layer in top_layers:
                x = layer(x, training=False)
            predictions = x
            if pred_index is None:
                pred_index = int(tf.argmax(predictions[0]))
            class_channel = predictions[:, pred_index]
    else:
        # Model datar → grad model fungsional standar.
        grad_model = tf.keras.models.Model(
            inputs=model.inputs,
            outputs=[feature_layer.output, model.output],
        )
        with tf.GradientTape() as tape:
            conv_outputs, predictions = grad_model(img_tensor)
            tape.watch(conv_outputs)
            if pred_index is None:
                pred_index = int(tf.argmax(predictions[0]))
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
