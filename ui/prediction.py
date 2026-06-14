import pandas as pd
import streamlit as st
from PIL import Image
from datetime import datetime

from config import ALLOWED_EXTENSIONS, MODEL_PATH
from utils.gradcam import create_gradcam_overlay
from utils.history_manager import save_history
from utils.model_loader import load_class_names, load_prediction_model
from utils.preprocessing import predict_image

def show_prediction():
    st.markdown("<h1 style='margin-bottom: 8px;'>Analisis Citra Feses</h1>", unsafe_allow_html=True)
    st.markdown("<p style='margin-bottom: 24px;'>Unggah gambar feses ayam untuk mendapatkan hasil screening penyakit.</p>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.2], gap="large")

    with col1:
        st.markdown("<div class='card' style='margin-bottom: 24px;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='font-size: 16px; margin-bottom: 12px;'>1. Upload Gambar</h3>", unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(
            "", 
            type=ALLOWED_EXTENSIONS,
            label_visibility="collapsed"
        )
        
        image = None
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.markdown("<h3 style='font-size: 16px; margin-top: 16px; margin-bottom: 8px;'>Preview</h3>", unsafe_allow_html=True)
            st.image(image, use_container_width=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

        predict_clicked = st.button("📊 Prediksi Sekarang", type="primary", use_container_width=True)
        
        st.markdown("""
<div style="background-color: #FFFBEB; border-left: 4px solid #FBBF24; padding: 12px; border-radius: 8px; margin-top: 16px;">
    <p style="margin: 0; font-size: 12px; color: #92400E;"><strong>Catatan:</strong> Hasil ini bukan diagnosis klinis. Pemeriksaan lebih lanjut tetap memerlukan dokter hewan atau ahli.</p>
</div>
        """, unsafe_allow_html=True)

    with col2:
        if uploaded_file is None:
            st.info("Silakan unggah gambar di kolom kiri untuk melihat hasil analisis.")
            return

        if predict_clicked:
            try:
                model = load_prediction_model()
                class_names = load_class_names()
            except Exception as exc:
                st.error("Gagal memuat model.")
                st.code(str(exc))
                return
                
            with st.spinner("Memproses analisis..."):
                pred_class, confidence, probabilities = predict_image(model, image, class_names)
                
                result_df = pd.DataFrame({
                    "Kelas": class_names,
                    "Probabilitas": probabilities,
                })
                result_df["Persentase"] = result_df["Probabilitas"] * 100
                result_df = result_df.sort_values("Probabilitas", ascending=False)
                
                color_map = {
                    "Healthy": "#2563EB", 
                    "Coccidiosis": "#DC2626", 
                    "Salmonella": "#D97706", 
                    "Newcastle Disease": "#7C3AED"
                }
                pred_color = color_map.get(pred_class, "#2563EB")
                
                # Container Hasil
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                
                st.markdown(f"""
<div style='display: flex; justify-content: space-between; border-bottom: 1px solid #E5E7EB; padding-bottom: 16px; margin-bottom: 16px;'>
    <div>
        <p style='font-size: 12px; font-weight: 600; color: #6B7280; text-transform: uppercase; margin: 0 0 4px 0;'>Kelas Terdeteksi</p>
        <h2 style='margin: 0; font-size: 28px; color: {pred_color};'>{pred_class}</h2>
    </div>
    <div style='text-align: right;'>
        <p style='font-size: 12px; font-weight: 600; color: #6B7280; text-transform: uppercase; margin: 0 0 4px 0;'>Confidence</p>
        <h2 style='margin: 0; font-size: 28px; color: #172033;'>{confidence * 100:.1f}%</h2>
    </div>
</div>
                """, unsafe_allow_html=True)
                
                # Probability bars
                bars_html = ""
                for _, row in result_df.iterrows():
                    cls_name = row['Kelas']
                    pct = row['Persentase']
                    bar_color = color_map.get(cls_name, "#9CA3AF")
                    
                    bars_html += f"""
<div style='margin-bottom: 12px;'>
    <div style='display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 4px; font-weight: 500;'>
        <span style='color: #172033;'>{cls_name}</span>
        <span style='color: #6B7280;'>{pct:.1f}%</span>
    </div>
    <div style='width: 100%; background-color: #F3F4F6; border-radius: 4px; height: 6px;'>
        <div style='background-color: {bar_color}; width: {pct}%; height: 100%; border-radius: 4px;'></div>
    </div>
</div>
                    """
                st.markdown(bars_html, unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Save history
                save_history({
                    "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "nama_file": uploaded_file.name,
                    "prediksi": pred_class,
                    "confidence": round(confidence * 100, 2),
                })
                
                # Grad-CAM
                st.markdown("<div class='card' style='margin-top: 24px;'>", unsafe_allow_html=True)
                st.markdown("<h3 style='font-size: 16px; margin-bottom: 16px;'>Visualisasi Grad-CAM</h3>", unsafe_allow_html=True)
                
                gcam1, gcam2 = st.columns(2)
                with gcam1:
                    st.markdown("<p style='font-size: 12px; font-weight: 600; text-align: center; margin-bottom: 8px;'>Gambar Asli</p>", unsafe_allow_html=True)
                    st.image(image, use_container_width=True)
                with gcam2:
                    st.markdown("<p style='font-size: 12px; font-weight: 600; text-align: center; margin-bottom: 8px;'>Hasil Grad-CAM</p>", unsafe_allow_html=True)
                    try:
                        overlay = create_gradcam_overlay(image, model)
                        st.image(overlay, use_container_width=True)
                    except Exception:
                        st.warning("Tidak dapat memproses Grad-CAM.")
                
                st.markdown("""
<p style='font-size: 12px; color: #6B7280; text-align: center; margin-top: 12px; margin-bottom: 0;'>
    Grad-CAM menampilkan area pada citra yang paling berkontribusi terhadap keputusan model.
</p>
                """, unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
