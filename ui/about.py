import streamlit as st

def show_about():
    st.markdown("<h1 style='margin-bottom: 8px;'>Tentang FesesScan Ayam</h1>", unsafe_allow_html=True)
    st.markdown("<p style='margin-bottom: 24px;'>Aplikasi screening awal penyakit ayam berbasis citra feses.</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
<div class='card' style='margin-bottom: 24px;'>
    <h3 style='font-size: 16px; margin-bottom: 8px;'>🎯 Tujuan Aplikasi</h3>
    <p style='font-size: 14px; line-height: 1.6;'>
        Membantu peternak dan tenaga medis hewan mengidentifikasi indikasi penyakit melalui feses ayam secara cepat sebagai screening awal.
    </p>
</div>
        """, unsafe_allow_html=True)

        st.markdown("""
<div class='card' style='margin-bottom: 24px;'>
    <h3 style='font-size: 16px; margin-bottom: 8px;'>📈 Metode Penelitian</h3>
    <p style='font-size: 14px; line-height: 1.6;'>
        Sistem menggunakan <strong>EfficientNet-B0 Direct Multiclass Classification</strong> untuk mengoptimalkan akurasi dan recall dalam mendeteksi 4 kategori utama.
    </p>
</div>
        """, unsafe_allow_html=True)

        st.markdown("""
<div class='card' style='margin-bottom: 24px;'>
    <h3 style='font-size: 16px; margin-bottom: 8px;'>👁️ Fitur Grad-CAM</h3>
    <p style='font-size: 14px; line-height: 1.6;'>
        Visualisasi peta panas (heat map) untuk memberikan interpretabilitas tentang area gambar yang menjadi fokus model saat melakukan prediksi.
    </p>
</div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
<div class='card' style='margin-bottom: 24px;'>
    <h3 style='font-size: 16px; margin-bottom: 16px;'>📊 Kelas Prediksi</h3>
    <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 12px;'>
        <div style='background-color: #F8FAFC; padding: 12px; border-radius: 8px; border: 1px solid #E5E7EB; text-align: center;'>
            <div style='font-size: 20px; margin-bottom: 4px;'>✅</div>
            <p style='margin: 0; font-size: 13px; font-weight: 600; color: #172033;'>Healthy</p>
        </div>
        <div style='background-color: #F8FAFC; padding: 12px; border-radius: 8px; border: 1px solid #E5E7EB; text-align: center;'>
            <div style='font-size: 20px; margin-bottom: 4px;'>🦠</div>
            <p style='margin: 0; font-size: 13px; font-weight: 600; color: #172033;'>Coccidiosis</p>
        </div>
        <div style='background-color: #F8FAFC; padding: 12px; border-radius: 8px; border: 1px solid #E5E7EB; text-align: center;'>
            <div style='font-size: 20px; margin-bottom: 4px;'>💊</div>
            <p style='margin: 0; font-size: 13px; font-weight: 600; color: #172033;'>Salmonella</p>
        </div>
        <div style='background-color: #F8FAFC; padding: 12px; border-radius: 8px; border: 1px solid #E5E7EB; text-align: center;'>
            <div style='font-size: 20px; margin-bottom: 4px;'>⚠️</div>
            <p style='margin: 0; font-size: 13px; font-weight: 600; color: #172033;'>Newcastle Disease</p>
        </div>
    </div>
</div>
        """, unsafe_allow_html=True)

        st.markdown("""
<div style='background-color: #FFFBEB; border: 1px solid #FDE68A; padding: 24px; border-radius: 12px; margin-bottom: 24px;'>
    <h3 style='font-size: 16px; margin-bottom: 8px; color: #92400E;'>⚠️ Keterbatasan Sistem</h3>
    <p style='font-size: 14px; line-height: 1.6; color: #92400E;'>
        Kualitas gambar sangat mempengaruhi prediksi. Ini bukan perangkat medis dan tidak menggantikan diagnosis dokter hewan profesional.
    </p>
</div>
        """, unsafe_allow_html=True)
