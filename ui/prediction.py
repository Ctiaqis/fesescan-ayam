import pandas as pd
import streamlit as st
from PIL import Image
from datetime import datetime

from config import ALLOWED_EXTENSIONS
from utils.gradcam import create_gradcam_overlay
from utils.history_manager import save_history
from utils.model_loader import load_class_names, load_prediction_model
from utils.preprocessing import predict_image


CLASS_META = {
    "Healthy":           {"icon": "✅", "color": "#059669", "bg": "#ECFDF5"},
    "Coccidiosis":       {"icon": "🦠", "color": "#DC2626", "bg": "#FEF2F2"},
    "Salmonella":        {"icon": "💊", "color": "#D97706", "bg": "#FFFBEB"},
    "Newcastle Disease": {"icon": "⚠️", "color": "#7C3AED", "bg": "#F5F3FF"},
}


def show_prediction():
    st.markdown("<h1 style='margin-bottom:4px;'>🔬 Analisis Citra Feses</h1>",
                unsafe_allow_html=True)
    st.markdown(
        "<p style='margin-bottom:24px;'>"
        "Unggah gambar feses ayam untuk mendapatkan hasil screening penyakit."
        "</p>",
        unsafe_allow_html=True,
    )

    left, right = st.columns([1, 1.3], gap="large")

    # ── Panel Kiri: Upload ────────────────────────────────────────────────────
    with left:
        with st.container(border=True):
            st.markdown("**📁 Upload Gambar**")
            uploaded_file = st.file_uploader(
                "Format JPG atau PNG",
                type=ALLOWED_EXTENSIONS,
                label_visibility="visible",
            )

        image = None
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            with st.container(border=True):
                st.markdown("**🖼️ Preview Gambar**")
                st.image(image, use_container_width=True)

        predict_clicked = st.button(
            "📊 Prediksi Sekarang",
            type="primary",
            use_container_width=True,
            disabled=(uploaded_file is None),
        )

        st.info(
            "Hasil ini bukan diagnosis klinis. "
            "Pemeriksaan lebih lanjut tetap memerlukan dokter hewan.",
            icon="ℹ️",
        )

    # ── Panel Kanan: Hasil ────────────────────────────────────────────────────
    with right:
        if uploaded_file is None:
            st.markdown("""
            <div class="fss-card" style="text-align:center; padding:48px 24px;">
                <div style="font-size:48px; margin-bottom:12px;">🔍</div>
                <div style="font-size:15px; font-weight:600; color:#1F1B2E;
                            margin-bottom:6px;">Belum Ada Gambar</div>
                <p style="font-size:13px; margin:0;">
                    Silakan unggah gambar di panel kiri untuk melihat hasil analisis.
                </p>
            </div>
            """, unsafe_allow_html=True)
            return

        if not predict_clicked:
            st.markdown("""
            <div class="fss-card" style="text-align:center; padding:48px 24px;">
                <div style="font-size:48px; margin-bottom:12px;">⏳</div>
                <div style="font-size:15px; font-weight:600; color:#1F1B2E;
                            margin-bottom:6px;">Siap Dianalisis</div>
                <p style="font-size:13px; margin:0;">
                    Klik tombol <strong>Prediksi Sekarang</strong> untuk memulai analisis.
                </p>
            </div>
            """, unsafe_allow_html=True)
            return

        # ── Jalankan prediksi ─────────────────────────────────────────────
        try:
            model = load_prediction_model()
            class_names = load_class_names()
        except Exception as exc:
            st.error(f"Gagal memuat model: {exc}")
            return

        with st.spinner("Memproses analisis, mohon tunggu…"):
            pred_class, confidence, probabilities = predict_image(
                model, image, class_names
            )

        meta = CLASS_META.get(pred_class, {"icon": "🔎", "color": "#7C3AED", "bg": "#EDE9FE"})

        # ── Hasil Utama ───────────────────────────────────────────────────
        with st.container(border=True):
            st.markdown("**Hasil Prediksi**")

            m1, m2 = st.columns(2)
            with m1:
                st.metric("Kelas Terdeteksi", f"{meta['icon']} {pred_class}")
            with m2:
                st.metric("Confidence", f"{confidence * 100:.1f}%")

            st.markdown("---")

            # ── Probability Bars ──────────────────────────────────────────
            st.markdown("**Distribusi Probabilitas**")
            st.write("")

            result_df = pd.DataFrame(
                {"Kelas": class_names, "Probabilitas": probabilities}
            ).sort_values("Probabilitas", ascending=False)

            for _, row in result_df.iterrows():
                cls = row["Kelas"]
                prob = float(row["Probabilitas"])
                m = CLASS_META.get(cls, {"icon": "·", "color": "#7C3AED", "bg": "#EDE9FE"})

                col_label, col_bar = st.columns([1, 2])
                with col_label:
                    st.markdown(
                        f"<div style='display:flex; align-items:center; gap:6px; "
                        f"padding:4px 0; font-size:13px; font-weight:600; color:#1F1B2E;'>"
                        f"{m['icon']} {cls}</div>",
                        unsafe_allow_html=True,
                    )
                with col_bar:
                    pct_label = f"{prob * 100:.1f}%"
                    st.progress(prob, text=pct_label)

        # ── Simpan riwayat ────────────────────────────────────────────────
        save_history({
            "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "nama_file": uploaded_file.name,
            "prediksi": pred_class,
            "confidence": round(confidence * 100, 2),
        })

        # ── Grad-CAM ──────────────────────────────────────────────────────
        with st.container(border=True):
            st.markdown("**👁️ Visualisasi Grad-CAM**")
            st.caption(
                "Grad-CAM menampilkan area pada citra yang paling berkontribusi "
                "terhadap keputusan model."
            )

            gcam_left, gcam_right = st.columns(2, gap="medium")
            with gcam_left:
                st.markdown(
                    "<p style='font-size:12px; font-weight:600; text-align:center;'>"
                    "Gambar Asli</p>",
                    unsafe_allow_html=True,
                )
                st.image(image, use_container_width=True)

            with gcam_right:
                st.markdown(
                    "<p style='font-size:12px; font-weight:600; text-align:center;'>"
                    "Hasil Grad-CAM</p>",
                    unsafe_allow_html=True,
                )
                try:
                    overlay = create_gradcam_overlay(image, model)
                    st.image(overlay, use_container_width=True)
                except Exception:
                    st.warning("Grad-CAM tidak dapat diproses untuk gambar ini.", icon="⚠️")
