import streamlit as st
from PIL import Image
import numpy as np

from config import APP_TITLE, APP_SUBTITLE, DISCLAIMER, ALLOWED_EXTENSIONS
from utils.model_loader import load_prediction_model, load_class_names
from utils.preprocessing import predict_image
from utils.gradcam import create_gradcam_overlay

st.set_page_config(page_title=APP_TITLE, layout="centered")

st.markdown(
    """
    <style>
    [data-testid="stImage"] img {
        object-fit: contain !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.title(APP_TITLE)
    st.write(APP_SUBTITLE)
    
    # Load model and classes
    try:
        model = load_prediction_model()
        class_names = load_class_names()
    except Exception as e:
        st.error(f"Error loading model atau config: {e}")
        return

    # Upload file
    uploaded_file = st.file_uploader(
        "Upload citra feses ayam", 
        type=ALLOWED_EXTENSIONS
    )
    
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Preview Gambar", use_container_width=True)
            
            if st.button("Prediksi", type="primary", use_container_width=True):
                with st.spinner("Menganalisis gambar..."):
                    # Prediksi
                    pred_class, confidence, probabilities = predict_image(model, image, class_names)
                    
                    st.success("Prediksi Selesai!")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Kelas Terdeteksi", pred_class)
                    with col2:
                        st.metric("Confidence Score", f"{confidence * 100:.2f}%")
                    
                    st.markdown("### Probabilitas tiap Kelas")
                    for cls_name, prob in zip(class_names, probabilities):
                        st.write(f"**{cls_name}**: {prob * 100:.2f}%")
                        st.progress(float(prob))
                        
                    st.markdown("### Visualisasi Grad-CAM")
                    with st.spinner("Membuat Grad-CAM..."):
                        overlay = create_gradcam_overlay(image, model)
                        st.image(overlay, caption="Area fokus model", use_container_width=True)
                        
        except Exception as e:
            st.error(f"Terjadi kesalahan saat memproses gambar: {e}")
                    
    st.markdown("---")
    st.info(DISCLAIMER)

if __name__ == "__main__":
    main()
