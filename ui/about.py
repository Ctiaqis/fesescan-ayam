import streamlit as st


def show_about():
    st.markdown("<h1 style='margin-bottom:4px;'>ℹ️ Tentang FesesScan Ayam</h1>",
                unsafe_allow_html=True)
    st.markdown(
        "<p style='margin-bottom:28px;'>"
        "Aplikasi screening awal penyakit ayam berbasis citra feses."
        "</p>",
        unsafe_allow_html=True,
    )

    left, right = st.columns(2, gap="large")

    # ── Kolom Kiri ────────────────────────────────────────────────────────────
    with left:
        # Tujuan
        st.markdown("<div class='fss-card'>", unsafe_allow_html=True)
        st.markdown("##### 🎯 Tujuan Aplikasi")
        st.markdown(
            "<p style='font-size:14px; line-height:1.7; margin:0;'>"
            "Membantu peternak dan tenaga medis hewan mengidentifikasi indikasi "
            "penyakit melalui feses ayam secara cepat sebagai <strong>screening awal</strong>, "
            "sehingga penanganan dapat dilakukan lebih dini."
            "</p>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

        # Metode
        st.markdown("<div class='fss-card'>", unsafe_allow_html=True)
        st.markdown("##### 📈 Metode Penelitian")
        st.markdown(
            "<p style='font-size:14px; line-height:1.7; margin:0;'>"
            "Sistem menggunakan <strong>EfficientNet-B0 Direct Multiclass "
            "Classification</strong> untuk mengoptimalkan akurasi dan recall "
            "dalam mendeteksi 4 kategori utama penyakit ayam."
            "</p>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

        # Grad-CAM
        st.markdown("<div class='fss-card'>", unsafe_allow_html=True)
        st.markdown("##### 👁️ Fitur Grad-CAM")
        st.markdown(
            "<p style='font-size:14px; line-height:1.7; margin:0;'>"
            "Visualisasi <em>heat map</em> yang menunjukkan area gambar yang "
            "menjadi fokus model saat melakukan prediksi, meningkatkan "
            "interpretabilitas hasil analisis."
            "</p>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # ── Kolom Kanan ───────────────────────────────────────────────────────────
    with right:
        # Kelas Prediksi
        st.markdown("<div class='fss-card'>", unsafe_allow_html=True)
        st.markdown("##### 📊 Kelas Prediksi")
        st.write("")

        classes = [
            ("✅", "#ECFDF5", "#065F46", "Healthy",
             "Feses normal, kondisi ayam sehat."),
            ("🦠", "#FEF2F2", "#991B1B", "Coccidiosis",
             "Infeksi parasit protozoa pada usus ayam."),
            ("💊", "#FFFBEB", "#92400E", "Salmonella",
             "Infeksi bakteri Salmonella spp."),
            ("⚠️", "#F5F3FF", "#4C1D95", "Newcastle Disease",
             "Infeksi virus paramyxovirus yang menular."),
        ]

        for icon, bg, color, name, desc in classes:
            st.markdown(f"""
            <div style="display:flex; align-items:flex-start; gap:14px;
                        background:{bg}; padding:14px 16px; border-radius:10px;
                        margin-bottom:10px;">
                <div style="font-size:22px; line-height:1; flex-shrink:0;">{icon}</div>
                <div>
                    <div style="font-size:14px; font-weight:700; color:{color};
                                margin-bottom:2px;">{name}</div>
                    <div style="font-size:13px; color:#6B6478; line-height:1.5;">{desc}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # Keterbatasan
        st.warning(
            "**Keterbatasan Sistem**\n\n"
            "Kualitas gambar sangat mempengaruhi akurasi prediksi. "
            "Aplikasi ini **bukan perangkat medis** dan tidak menggantikan "
            "diagnosis dokter hewan profesional.",
            icon="⚠️",
        )