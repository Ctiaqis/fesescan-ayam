import numpy as np
from PIL import Image
from tensorflow.keras.applications.efficientnet import preprocess_input

from config import IMG_SIZE


def preprocess_image(image: Image.Image):
    """Preprocessing gambar agar sesuai dengan input EfficientNetB0.

    Catatan: preprocessing ini mengikuti training notebook, yaitu resize ke 224x224
    dan EfficientNet preprocess_input.
    """
    image = image.convert("RGB")
    image = image.resize(IMG_SIZE)

    image_array = np.array(image).astype(np.float32)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = preprocess_input(image_array)
    return image_array


def predict_image(model, image: Image.Image, class_names):
    input_array = preprocess_image(image)
    probabilities = model.predict(input_array, verbose=0)[0]

    pred_index = int(np.argmax(probabilities))
    pred_class = class_names[pred_index]
    confidence = float(probabilities[pred_index])

    return pred_class, confidence, probabilities, pred_index
