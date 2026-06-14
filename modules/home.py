import streamlit as st

from config import APP_TITLE, DISCLAIMER


def show_home():
    st.title(APP_TITLE)
    st.write(
        """
        Dashboard ini digunakan sebagai prototipe web untuk melakukan **screening awal**
        penyakit ayam berdasarkan citra feses. Model final yang digunakan adalah
        **EfficientNetB0 Direct Multiclass**.
        """
    )

    st.warning(DISCLAIMER)

    st.subheader("Kelas Prediksi")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Kelas 1", "Healthy")
    col2.metric("Kelas 2", "Coccidiosis")
    col3.metric("Kelas 3", "Salmonella")
    col4.metric("Kelas 4", "Newcastle Disease")

    st.subheader("Alur Sistem")
    st.code(
        """
Upload gambar feses ayam
        ↓
Preprocessing gambar 224×224
        ↓
Model EfficientNetB0 Direct Multiclass
        ↓
Prediksi 4 kelas
        ↓
Hasil prediksi + confidence score
        """,
        language="text",
    )

    st.subheader("Alasan Model Dipilih")
    st.write(
        """
        Model **EfficientNetB0 Direct Multiclass** dipilih karena memiliki recall
        tertinggi pada kelas minoritas **Newcastle Disease** dan tidak memiliki risiko
        **error propagation** seperti pada pendekatan two-stage. Hal ini lebih sesuai
        dengan tujuan sistem sebagai screening awal.
        """
    )
