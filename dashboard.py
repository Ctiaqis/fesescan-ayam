import streamlit as st
from PIL import Image
import numpy as np

from config import APP_TITLE, APP_SUBTITLE, DISCLAIMER, ALLOWED_EXTENSIONS
from utils.model_loader import load_prediction_model, load_class_names
from utils.preprocessing import predict_image
from utils.gradcam import create_gradcam_overlay
from styles import SHADCN_CSS

st.set_page_config(page_title=APP_TITLE, page_icon="🐔", layout="centered")

st.markdown(SHADCN_CSS, unsafe_allow_html=True)


def hero():
    st.markdown(
        """
        <div class="hero">
            <div class="hero-row">
                <div class="logo">🐔</div>
                <div>
                    <span class="hero-badge">AI Screening · Grad-CAM</span>
                    <div class="hero-title">Screening Awal Penyakit Ayam</div>
                    <p class="hero-sub">Deteksi dini berbasis citra feses · EfficientNetB0 Direct Multiclass</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section(label: str, icon: str = ""):
    st.markdown(
        f'<div class="section-label">{icon} {label}</div>',
        unsafe_allow_html=True,
    )


def render_probabilities(class_names, probabilities, pred_class):
    section("Probabilitas tiap Kelas", "📊")
    pairs = sorted(zip(class_names, probabilities), key=lambda x: x[1], reverse=True)
    for cls_name, prob in pairs:
        pct = float(prob) * 100
        top = "top" if cls_name == pred_class else ""
        st.markdown(
            f"""
            <div class="prob-row">
                <div class="prob-head">
                    <span class="prob-name {top}">{cls_name}</span>
                    <span class="prob-val {top}">{pct:.2f}%</span>
                </div>
                <div class="prob-track">
                    <div class="prob-fill {top}" style="width:{pct:.2f}%"></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def main():
    hero()

    try:
        model = load_prediction_model()
        class_names = load_class_names()
    except Exception as e:
        st.error(f"Error loading model atau config: {e}")
        return

    section("Unggah Citra", "📤")
    uploaded_file = st.file_uploader(
        "Upload citra feses ayam",
        type=ALLOWED_EXTENSIONS,
        label_visibility="collapsed",
    )

    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Preview Gambar", use_container_width=True)

            if st.button("🔍 Prediksi Sekarang", type="primary", use_container_width=True):
                with st.spinner("Menganalisis gambar..."):
                    pred_class, confidence, probabilities = predict_image(
                        model, image, class_names
                    )

                st.success("Prediksi selesai!")

                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Kelas Terdeteksi", pred_class)
                with col2:
                    st.metric("Confidence Score", f"{confidence * 100:.2f}%")

                render_probabilities(class_names, probabilities, pred_class)

                section("Visualisasi Grad-CAM", "🔥")
                with st.spinner("Membuat Grad-CAM..."):
                    overlay = create_gradcam_overlay(image, model)
                    st.image(
                        overlay,
                        caption="Area fokus model saat memprediksi",
                        use_container_width=True,
                    )

        except Exception as e:
            st.error(f"Terjadi kesalahan saat memproses gambar: {e}")

    st.markdown(
        f"""
        <div class="disclaimer">
            <span class="ico">ℹ️</span>
            <span>{DISCLAIMER}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
