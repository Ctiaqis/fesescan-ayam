import streamlit as st

from ui.home import show_home
from ui.prediction import show_prediction
from ui.history import show_history
from ui.about import show_about

def inject_global_css():
    st.markdown("""
    <style>
        /* Sembunyikan default header, footer, dan menu Streamlit */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Main background & Text colors */
        .stApp {
            background-color: #F6FAFF;
            color: #172033;
        }
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #07111F !important;
            border-right: none !important;
            min-width: 260px !important;
            max-width: 260px !important;
        }
        [data-testid="stSidebar"] * {
            color: #FFFFFF;
        }
        
        /* Styling Radio di Sidebar agar menjadi menu */
        .stRadio > div[role="radiogroup"] > label {
            background: transparent;
            padding: 12px 16px !important;
            border-radius: 8px !important;
            margin-bottom: 4px !important;
            cursor: pointer;
            transition: 0.2s;
        }
        .stRadio > div[role="radiogroup"] > label:hover {
            background-color: #102A43 !important;
            color: #FFFFFF !important;
        }
        .stRadio > div[role="radiogroup"] > label[data-checked="true"] {
            background-color: #102A43 !important;
            border-left: 4px solid #38BDF8 !important;
            border-radius: 0 8px 8px 0 !important;
        }
        .stRadio > div[role="radiogroup"] > label[data-checked="true"] p {
            color: #38BDF8 !important;
            font-weight: 600 !important;
        }
        /* Hide radio circle */
        .stRadio > div[role="radiogroup"] > label > div:first-child {
            display: none !important;
        }
        
        /* Custom UI containers */
        .card {
            background-color: #FFFFFF;
            padding: 24px;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            border: 1px solid #E5E7EB;
        }
        
        /* Styling Buttons natively */
        .stButton > button {
            background-color: #2563EB !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 10px 20px !important;
            font-weight: 600 !important;
        }
        .stButton > button:hover {
            background-color: #1D4ED8 !important;
            color: #FFFFFF !important;
        }
        .stButton > button[kind="secondary"] {
            background-color: transparent !important;
            color: #172033 !important;
            border: 1px solid #D1D5DB !important;
        }
        .stButton > button[kind="secondary"]:hover {
            background-color: #F3F4F6 !important;
        }
        
        /* H1, H2, H3 colors */
        h1, h2, h3 {
            color: #172033 !important;
            font-family: sans-serif;
        }
        p {
            color: #6B7280;
        }
    </style>
    """, unsafe_allow_html=True)

def render_dashboard():
    inject_global_css()
    
    # Sidebar Header (Logo dan Judul)
    st.sidebar.markdown("""
    <div style='display: flex; align-items: center; gap: 12px; margin-bottom: 30px; margin-top: -30px;'>
        <div style='background-color: #2563EB; width: 40px; height: 40px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 20px;'>
            🐔
        </div>
        <div>
            <h2 style='margin: 0; font-size: 18px; color: #FFFFFF !important; font-weight: 700;'>FesesScan Ayam</h2>
            <p style='margin: 0; font-size: 11px; color: #94A3B8; text-transform: uppercase;'>Screening Penyakit Ayam</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Menu
    menu = st.sidebar.radio(
        "",
        ["Beranda", "Prediksi", "Riwayat", "Tentang"],
        index=0
    )
    
    # Push content to bottom
    st.sidebar.markdown("<div style='flex-grow: 1; min-height: 40vh;'></div>", unsafe_allow_html=True)
    
    # Sidebar Footer (Model Info)
    st.sidebar.markdown("""
    <div style='background-color: #102A43; padding: 16px; border-radius: 12px; margin-top: 20px;'>
        <p style='margin: 0 0 8px 0; color: #94A3B8; font-size: 11px; text-transform: uppercase; font-weight: 600;'>Informasi Model</p>
        <p style='margin: 0 0 8px 0; color: #FFFFFF; font-size: 13px; font-weight: 500;'>EfficientNetB0 Direct Multiclass</p>
        <p style='margin: 0; color: #94A3B8; font-size: 11px;'>Kelas: Healthy, Coccidiosis, Salmonella, Newcastle Disease</p>
    </div>
    """, unsafe_allow_html=True)

    # Routing
    if menu == "Beranda":
        show_home()
    elif menu == "Prediksi":
        show_prediction()
    elif menu == "Riwayat":
        show_history()
    elif menu == "Tentang":
        show_about()
