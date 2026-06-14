import streamlit as st

from ui.home import show_home
from ui.prediction import show_prediction
from ui.history import show_history
from ui.about import show_about


def inject_global_css():
    st.markdown("""
    <style>
        /* Header transparan; hanya elemen pengganggu yang disembunyikan. */
        header[data-testid="stHeader"] {
            background: transparent !important;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        [data-testid="stToolbar"] {display: none !important;}
        [data-testid="stDecoration"] {display: none !important;}
        [data-testid="stStatusWidget"] {display: none !important;}

        .stApp {
            background-color: #FAF7FF;
            color: #1F1B2E;
        }

        /* Sidebar — DIPAKSA SELALU TAMPIL agar tidak bisa "hilang" saat
           di-collapse. Override semua mekanisme collapse Streamlit. */
        [data-testid="stSidebar"] {
            background-color: #1F1B2E !important;
            width: 256px !important;
            min-width: 256px !important;
            max-width: 256px !important;
            transform: none !important;
            margin-left: 0 !important;
            left: 0 !important;
            visibility: visible !important;
        }
        [data-testid="stSidebar"][aria-expanded="false"] {
            transform: none !important;
            margin-left: 0 !important;
        }
        [data-testid="stSidebar"] * {
            color: #FFFFFF !important;
        }
        /* Sembunyikan tombol collapse agar sidebar tidak bisa ditutup
           (mencegah masalah sidebar hilang dan tidak bisa dibuka lagi). */
        [data-testid="stSidebarCollapseButton"],
        [data-testid="stSidebarHeader"] button {
            display: none !important;
        }

        /* Radio sebagai menu navigasi */
        [data-testid="stSidebar"] .stRadio [role="radiogroup"] label {
            background: transparent;
            padding: 11px 14px !important;
            border-radius: 8px !important;
            margin-bottom: 4px !important;
            cursor: pointer;
            transition: background 0.15s, color 0.15s;
        }
        [data-testid="stSidebar"] .stRadio [role="radiogroup"] label:hover {
            background-color: #2D2640 !important;
        }
        /* Sembunyikan lingkaran radio bawaan */
        [data-testid="stSidebar"] .stRadio [role="radiogroup"] label > div:first-child {
            display: none !important;
        }
        /* Item menu yang sedang aktif */
        [data-testid="stSidebar"] .stRadio [role="radiogroup"] label:has(input:checked) {
            background-color: #7C3AED !important;
        }
        [data-testid="stSidebar"] .stRadio [role="radiogroup"] label:has(input:checked) p {
            color: #FFFFFF !important;
            font-weight: 700 !important;
        }
        [data-testid="stSidebar"] .stRadio [role="radiogroup"] label p {
            color: #C4B5FD !important;
            font-size: 14px !important;
        }

        /* Card komponen (HTML mandiri dalam satu blok markdown) */
        .fss-card {
            background-color: #FFFFFF;
            padding: 24px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(124, 58, 237, 0.07);
            border: 1px solid #EDE9FE;
            margin-bottom: 16px;
        }

        /* Card via st.container(border=True) — bungkus konten Streamlit asli */
        [data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #FFFFFF;
            border: 1px solid #EDE9FE !important;
            border-radius: 12px !important;
            box-shadow: 0 2px 8px rgba(124, 58, 237, 0.07);
        }

        /* Tombol utama */
        .stButton > button {
            background-color: #7C3AED !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 10px 20px !important;
            font-weight: 600 !important;
            transition: background 0.2s !important;
        }
        /* Paksa teks di dalam tombol ikut warna tombol (kalahkan aturan p global) */
        .stButton > button p,
        .stButton > button span,
        .stButton > button div {
            color: inherit !important;
        }
        .stButton > button:hover {
            background-color: #6D28D9 !important;
        }
        .stButton > button[kind="secondary"] {
            background-color: #FFFFFF !important;
            color: #1F1B2E !important;
            border: 1px solid #D1D5DB !important;
        }
        .stButton > button[kind="secondary"]:hover {
            background-color: #F5F3FF !important;
        }

        /* File uploader — selaraskan dengan tema ungu */
        [data-testid="stFileUploaderDropzone"] {
            background-color: #F5F3FF !important;
            border: 1.5px dashed #C4B5FD !important;
            border-radius: 10px !important;
        }
        [data-testid="stFileUploaderDropzone"] * {
            color: #4C1D95 !important;
        }
        [data-testid="stFileUploaderDropzone"] button {
            background-color: #7C3AED !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
        }
        [data-testid="stFileUploaderDropzone"] button:hover {
            background-color: #6D28D9 !important;
        }
        [data-testid="stFileUploaderDropzone"] button * {
            color: #FFFFFF !important;
        }
        /* Chip file yang sudah diunggah */
        [data-testid="stFileUploaderFile"] {
            background-color: #F5F3FF !important;
            border-radius: 8px !important;
            padding: 4px 8px !important;
        }
        [data-testid="stFileUploaderFile"] * {
            color: #1F1B2E !important;
        }

        /* Heading */
        h1, h2, h3, h4 {
            color: #1F1B2E !important;
        }
        p {
            color: #6B6478;
        }

        /* Progress bar warna */
        .stProgress > div > div > div {
            background-color: #7C3AED !important;
        }

        /* Metric */
        [data-testid="stMetricValue"] {
            color: #7C3AED !important;
            font-size: 28px !important;
            font-weight: 700 !important;
        }
        [data-testid="stMetricLabel"] {
            color: #6B6478 !important;
            font-size: 12px !important;
            font-weight: 600 !important;
            text-transform: uppercase !important;
        }

        /* Info box — selaraskan dengan tema ungu */
        .stAlert {
            border-radius: 10px !important;
        }
        [data-testid="stAlert"] {
            background-color: #F3EEFF !important;
            border: 1px solid #DDD6FE !important;
            border-left: 4px solid #7C3AED !important;
        }
        [data-testid="stAlert"] * {
            color: #3B0764 !important;
        }

        /* Divider warna */
        hr {
            border-top: 1px solid #EDE9FE !important;
        }
    </style>
    """, unsafe_allow_html=True)


def render_dashboard():
    inject_global_css()

    # Sidebar header
    st.sidebar.markdown("""
    <div style="display:flex; align-items:center; gap:12px; padding:8px 0 28px 0;">
        <div style="background:#7C3AED; width:40px; height:40px; border-radius:10px;
                    display:flex; align-items:center; justify-content:center; font-size:22px; flex-shrink:0;">
            🐔
        </div>
        <div>
            <div style="font-size:16px; font-weight:700; color:#FFFFFF; line-height:1.2;">FesesScan Ayam</div>
            <div style="font-size:11px; color:#A78BFA; text-transform:uppercase; letter-spacing:.05em;">
                Screening Penyakit Ayam
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    menu = st.sidebar.radio(
        "Menu navigasi",
        ["🏠  Beranda", "🔬  Prediksi", "📋  Riwayat", "ℹ️  Tentang"],
        index=0,
        label_visibility="collapsed",
    )

    st.sidebar.markdown("<div style='min-height:200px;'></div>", unsafe_allow_html=True)

    # Sidebar footer model info
    st.sidebar.markdown("""
    <div style="background:#2D2640; padding:14px 16px; border-radius:10px; border:1px solid #3B3060;">
        <div style="font-size:10px; color:#A78BFA; text-transform:uppercase; font-weight:600; margin-bottom:6px;">
            Informasi Model
        </div>
        <div style="font-size:13px; font-weight:600; color:#FFFFFF; margin-bottom:4px;">
            EfficientNet-B0
        </div>
        <div style="font-size:11px; color:#9CA3AF; line-height:1.5;">
            Direct Multiclass Classification<br>
            Healthy · Coccidiosis · Salmonella · Newcastle
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Routing
    label = menu.split("  ", 1)[-1]
    if label == "Beranda":
        show_home()
    elif label == "Prediksi":
        show_prediction()
    elif label == "Riwayat":
        show_history()
    elif label == "Tentang":
        show_about()