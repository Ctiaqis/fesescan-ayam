import streamlit as st
from config import APP_TITLE

# Konfigurasi halaman harus dipanggil pertama kali
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🐔",
    layout="wide",
    initial_sidebar_state="expanded",
)

from ui.dashboard import render_dashboard

if __name__ == "__main__":
    render_dashboard()
