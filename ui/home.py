import streamlit as st

def show_home():
    st.markdown("""
<div style="background: linear-gradient(135deg, #2563EB 0%, #1E40AF 100%); border-radius: 16px; padding: 40px; color: #FFFFFF; display: flex; align-items: center; justify-content: space-between; min-height: 300px; margin-bottom: 32px; box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.2);">
    <div style="flex: 1; padding-right: 32px;">
        <h1 style="font-size: 36px; font-weight: 800; margin-bottom: 8px; color: #FFFFFF !important;">FesesScan Ayam</h1>
        <h3 style="font-size: 18px; font-weight: 500; margin-bottom: 16px; color: #DBEAFE !important;">Screening Awal Penyakit Ayam Berbasis Citra Feses</h3>
        <p style="font-size: 15px; margin-bottom: 24px; line-height: 1.6; color: #EFF6FF;">
            Aplikasi ini membantu proses screening awal kondisi kesehatan ayam menggunakan teknologi machine learning berdasarkan citra feses.
        </p>
        <div style="display: flex; gap: 12px;">
            <div style="background-color: #FFFFFF; color: #2563EB; padding: 10px 20px; border-radius: 8px; font-weight: 600; font-size: 14px; text-align: center; display: inline-block;">Mulai Prediksi</div>
            <div style="background-color: rgba(255, 255, 255, 0.1); border: 1px solid #BFDBFE; color: #FFFFFF; padding: 10px 20px; border-radius: 8px; font-weight: 600; font-size: 14px; text-align: center; display: inline-block;">Pelajari Aplikasi</div>
        </div>
    </div>
    <div style="flex: 0.6; display: flex; justify-content: center; align-items: center;">
        <div style="width: 200px; height: 200px; background-color: #DBEAFE; border-radius: 50%; display: flex; justify-content: center; align-items: center; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
            <span style="font-size: 100px;">🐓</span>
        </div>
    </div>
</div>
    """, unsafe_allow_html=True)

    # 3 Cards Section
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
<div class="card" style="height: 100%;">
    <div style="background: #EFF6FF; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 16px; color: #2563EB; font-size: 24px;">📤</div>
    <h3 style="font-size: 16px; margin-bottom: 8px;">Upload Citra</h3>
    <p style="font-size: 13px; margin: 0;">Unggah gambar feses ayam dalam format JPG atau PNG untuk dianalisis.</p>
</div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
<div class="card" style="height: 100%;">
    <div style="background: #ECFEFF; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 16px; color: #0891B2; font-size: 24px;">🧠</div>
    <h3 style="font-size: 16px; margin-bottom: 8px;">Analisis AI</h3>
    <p style="font-size: 13px; margin: 0;">Model klasifikasi memproses pola pada citra untuk mendeteksi penyakit.</p>
</div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
<div class="card" style="height: 100%;">
    <div style="background: #FEF2F2; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 16px; color: #DC2626; font-size: 24px;">📊</div>
    <h3 style="font-size: 16px; margin-bottom: 8px;">Hasil Screening</h3>
    <p style="font-size: 13px; margin: 0;">Mendapatkan probabilitas kelas penyakit beserta interpretasi Grad-CAM.</p>
</div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # 4 Category Cards
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("""
<div style="background: #FFFFFF; padding: 16px; border-radius: 12px; border: 1px solid #E5E7EB; display: flex; align-items: center; gap: 12px;">
    <div style="background: #ECFEFF; padding: 10px; border-radius: 8px; font-size: 20px;">✅</div>
    <div>
        <h4 style="margin: 0; font-size: 14px; font-weight: 600; color: #172033;">Healthy</h4>
    </div>
</div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
<div style="background: #FFFFFF; padding: 16px; border-radius: 12px; border: 1px solid #E5E7EB; display: flex; align-items: center; gap: 12px;">
    <div style="background: #FEF2F2; padding: 10px; border-radius: 8px; font-size: 20px;">🦠</div>
    <div>
        <h4 style="margin: 0; font-size: 14px; font-weight: 600; color: #172033;">Coccidiosis</h4>
    </div>
</div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
<div style="background: #FFFFFF; padding: 16px; border-radius: 12px; border: 1px solid #E5E7EB; display: flex; align-items: center; gap: 12px;">
    <div style="background: #FFFBEB; padding: 10px; border-radius: 8px; font-size: 20px;">💊</div>
    <div>
        <h4 style="margin: 0; font-size: 14px; font-weight: 600; color: #172033;">Salmonella</h4>
    </div>
</div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown("""
<div style="background: #FFFFFF; padding: 16px; border-radius: 12px; border: 1px solid #E5E7EB; display: flex; align-items: center; gap: 12px;">
    <div style="background: #F5F3FF; padding: 10px; border-radius: 8px; font-size: 20px;">⚠️</div>
    <div>
        <h4 style="margin: 0; font-size: 14px; font-weight: 600; color: #172033;">Newcastle Disease</h4>
    </div>
</div>
        """, unsafe_allow_html=True)

    st.write("")

    # Disclaimer
    st.markdown("""
<div style="background-color: #FFFBEB; border-left: 4px solid #FBBF24; padding: 16px; border-radius: 8px; margin-top: 16px;">
    <p style="margin: 0; font-size: 13px; color: #92400E;"><strong>Perhatian:</strong> Hasil prediksi hanya sebagai bantuan screening awal dan bukan pengganti diagnosis dokter hewan. Selalu konsultasikan kondisi ternak Anda kepada tenaga medis profesional.</p>
</div>
    """, unsafe_allow_html=True)
