import streamlit as st

st.set_page_config(
    page_title="FesesScan Ayam",
    page_icon="🐔",
    layout="wide",
    initial_sidebar_state="expanded",
)

from ui.dashboard import render_dashboard

if __name__ == "__main__":
    render_dashboard()