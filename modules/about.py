import streamlit as st

from config import DISCLAIMER


def show_about():
    st.title("Tentang Dashboard")

    st.subheader("Deskripsi")
    st.write(
        """
        Dashboard ini dibuat sebagai prototipe untuk mendukung screening awal penyakit ayam
        berbasis citra feses. Sistem menggunakan model **EfficientNetB0 Direct Multiclass**
        yang memprediksi gambar ke dalam empat kelas.
        """
    )

    st.subheader("Kelas Prediksi")
    st.markdown(
        """
        - **Healthy**
        - **Coccidiosis**
        - **Salmonella**
        - **Newcastle Disease**
        """
    )

    st.subheader("Alasan Pemilihan Model")
    st.write(
        """
        EfficientNetB0 Direct Multiclass dipilih karena memiliki recall tertinggi pada
        kelas minoritas Newcastle Disease dan tidak memiliki risiko error propagation.
        Walaupun pendekatan two-stage memperoleh macro F1-score tertinggi, model direct
        lebih aman untuk kebutuhan screening awal yang menekankan sensitivitas terhadap
        penyakit minoritas.
        """
    )

    st.subheader("Batasan")
    st.warning(DISCLAIMER)
