import streamlit as st

from ui.home import show_home
from ui.prediction import show_prediction
from ui.history import show_history
from ui.about import show_about


def inject_global_css():
    st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}

        .stApp {
            background-color: #FAF7FF;
            color: #1F1B2E;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #1F1B2E !important;
            min-width: 256px !important;
            max-width: 256px !important;
        }
        [data-testid="stSidebar"] * {
            color: #FFFFFF !important;
        }

        /* Radio sebagai menu navigasi */
        .stRadio > div[role="radiogroup"] > label {
            background: transparent;
            padding: 12px 16px !important;
            border-radius: 8px !important;
            margin-bottom: 2px !important;
            cursor: pointer;
            transition: background 0.2s;
        }
        .stRadio > div[role="radiogroup"] > label:hover {
            background-color: #2D2640 !important;
        }
        .stRadio > div[role="radiogroup"] > label[data-checked="true"] {
            background-color: #3B0764 !important;
            border-left: 3px solid #A78BFA !important;
            border-radius: 0 8px 8px 0 !important;
        }
        .stRadio > div[role="radiogroup"] > label[data-checked="true"] p {
            color: #DDD6FE !important;
            font-weight: 600 !important;
        }
        .stRadio > div[role="radiogroup"] > label > div:first-child {
            display: none !important;
        }

        /* Card komponen */
        .fss-card {
            background-color: #FFFFFF;
            padding: 24px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(124, 58, 237, 0.07);
            border: 1px solid #EDE9FE;
            margin-bottom: 16px;
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

        /* Info box */
        .stAlert {
            border-radius: 10px !important;
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
        "",
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