import streamlit as st


def show_home():
    # ── Hero Banner ──────────────────────────────────────────────────────────
    st.markdown("""
    <div style="background:linear-gradient(135deg,#7C3AED 0%,#5B21B6 100%);
                border-radius:16px; padding:40px 36px; color:#FFFFFF;
                box-shadow:0 8px 24px rgba(124,58,237,0.25); margin-bottom:28px;">
        <div style="max-width:600px;">
            <div style="font-size:13px; font-weight:600; color:#DDD6FE;
                        text-transform:uppercase; letter-spacing:.08em; margin-bottom:8px;">
                🐔 Teknologi Machine Learning untuk Peternakan
            </div>
            <h1 style="font-size:34px; font-weight:800; color:#FFFFFF !important;
                       margin:0 0 10px 0; line-height:1.2;">FesesScan Ayam</h1>
            <p style="font-size:15px; color:#EDE9FE; line-height:1.7; margin:0 0 24px 0;">
                Screening awal penyakit ayam berbasis citra feses menggunakan model
                <strong style="color:#FFFFFF;">EfficientNet-B0</strong>.
                Upload gambar, analisis, dan dapatkan hasil dalam hitungan detik.
            </p>
            <div style="display:inline-block; background:#FFFFFF; color:#7C3AED;
                        padding:10px 22px; border-radius:8px; font-weight:700;
                        font-size:14px; cursor:pointer;">
                Mulai Prediksi →
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── 3 Fitur Utama ─────────────────────────────────────────────────────────
    st.markdown("#### Cara Kerja Aplikasi")
    st.write("")
    c1, c2, c3 = st.columns(3, gap="medium")

    features = [
        ("📤", "#EDE9FE", "#7C3AED", "1. Upload Citra",
         "Unggah foto feses ayam format JPG atau PNG langsung dari perangkat Anda."),
        ("🧠", "#FCE7F3", "#DB2777", "2. Analisis AI",
         "Model deep learning memproses pola visual pada citra secara otomatis."),
        ("📊", "#FEF3C7", "#D97706", "3. Hasil Screening",
         "Lihat probabilitas tiap kelas penyakit beserta visualisasi Grad-CAM."),
    ]

    for col, (icon, bg, color, title, desc) in zip([c1, c2, c3], features):
        with col:
            st.markdown(f"""
            <div class="fss-card" style="height:100%; text-align:left;">
                <div style="background:{bg}; width:48px; height:48px; border-radius:12px;
                            display:flex; align-items:center; justify-content:center;
                            font-size:22px; margin-bottom:14px;">{icon}</div>
                <div style="font-size:15px; font-weight:700; color:#1F1B2E;
                            margin-bottom:6px;">{title}</div>
                <p style="font-size:13px; margin:0; line-height:1.6;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.write("")
    st.markdown("---")

    # ── 4 Kelas Penyakit ──────────────────────────────────────────────────────
    st.markdown("#### Kelas yang Dapat Dideteksi")
    st.write("")

    classes = [
        ("✅", "#ECFDF5", "#065F46", "Healthy", "Feses normal, ayam sehat."),
        ("🦠", "#FEF2F2", "#991B1B", "Coccidiosis", "Infeksi parasit protozoa pada usus."),
        ("💊", "#FFFBEB", "#92400E", "Salmonella", "Infeksi bakteri Salmonella spp."),
        ("⚠️", "#F5F3FF", "#4C1D95", "Newcastle Disease", "Infeksi virus paramyxovirus."),
    ]

    cols = st.columns(4, gap="medium")
    for col, (icon, bg, text_color, name, desc) in zip(cols, classes):
        with col:
            st.markdown(f"""
            <div class="fss-card" style="text-align:center; padding:20px 16px;">
                <div style="font-size:28px; margin-bottom:8px;">{icon}</div>
                <div style="font-size:14px; font-weight:700; color:{text_color};
                            margin-bottom:4px;">{name}</div>
                <p style="font-size:12px; margin:0; line-height:1.5;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.write("")

    # ── Disclaimer ────────────────────────────────────────────────────────────
    st.warning(
        "**Perhatian:** Hasil prediksi hanya sebagai bantuan screening awal dan bukan "
        "pengganti diagnosis dokter hewan. Selalu konsultasikan kondisi ternak Anda "
        "kepada tenaga medis profesional.",
        icon="⚠️",
    )