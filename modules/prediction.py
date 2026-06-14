from datetime import datetime

import pandas as pd
import streamlit as st
from PIL import Image

from config import ALLOWED_EXTENSIONS, DISCLAIMER, MODEL_PATH
from utils.gradcam import create_gradcam_overlay
from utils.history_manager import save_history
from utils.model_loader import load_class_names, load_prediction_model
from utils.preprocessing import predict_image


def show_prediction():
    st.title("Prediksi Citra Feses Ayam")
    st.write(
        """
        Upload gambar feses ayam, lalu sistem akan menampilkan hasil prediksi,
        confidence score, probabilitas setiap kelas, dan visualisasi Grad-CAM jika tersedia.
        """
    )

    st.warning(DISCLAIMER)

    uploaded_file = st.file_uploader(
        "Upload gambar feses ayam",
        type=ALLOWED_EXTENSIONS,
    )

    if uploaded_file is None:
        st.info("Silakan upload gambar terlebih dahulu.")
        return

    try:
        model = load_prediction_model()
        class_names = load_class_names()
    except Exception as exc:
        st.error("Model belum bisa dimuat.")
        st.code(str(exc), language="text")
        st.info(f"Pastikan file model ada di: {MODEL_PATH}")
        return

    image = Image.open(uploaded_file)

    left_col, right_col = st.columns([1, 1])

    with left_col:
        st.subheader("Gambar Input")
        st.image(image, caption=uploaded_file.name, use_container_width=True)

    with right_col:
        st.subheader("Hasil Prediksi")

        if st.button("Mulai Prediksi", type="primary"):
            pred_class, confidence, probabilities = predict_image(model, image, class_names)

            result_df = pd.DataFrame({
                "Kelas": class_names,
                "Probabilitas": probabilities,
            })
            result_df["Persentase"] = result_df["Probabilitas"] * 100
            result_df = result_df.sort_values("Probabilitas", ascending=False)

            st.success(f"Hasil prediksi: **{pred_class}**")
            st.metric("Confidence Score", f"{confidence * 100:.2f}%")

            st.subheader("Probabilitas Setiap Kelas")
            for _, row in result_df.iterrows():
                st.write(f"**{row['Kelas']}**: {row['Persentase']:.2f}%")
                st.progress(float(row["Probabilitas"]))

            st.dataframe(
                result_df[["Kelas", "Persentase"]],
                use_container_width=True,
                hide_index=True,
            )

            save_history({
                "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "nama_file": uploaded_file.name,
                "prediksi": pred_class,
                "confidence": round(confidence * 100, 2),
            })

            st.subheader("Grad-CAM")
            try:
                overlay = create_gradcam_overlay(image, model)
                st.image(overlay, caption="Visualisasi area yang diperhatikan model", use_container_width=True)
            except Exception as exc:
                st.warning(
                    "Grad-CAM belum dapat ditampilkan untuk struktur model ini, "
                    "tetapi prediksi utama tetap berhasil."
                )
                with st.expander("Detail error Grad-CAM"):
                    st.code(str(exc), language="text")

            st.info(
                "Confidence score menunjukkan tingkat keyakinan model terhadap hasil prediksi. "
                "Hasil ini tetap perlu dikonfirmasi melalui pemeriksaan lanjutan."
            )
