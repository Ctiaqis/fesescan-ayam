import streamlit as st

from config import APP_TITLE, APP_SUBTITLE
from modules.home import show_home
from modules.prediction import show_prediction
from modules.history import show_history
from modules.about import show_about


st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🐔",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    st.sidebar.title("🐔 Screening Feses Ayam")
    st.sidebar.caption(APP_SUBTITLE)

    menu = st.sidebar.radio(
        "Menu",
        ["Beranda", "Prediksi", "Riwayat", "Tentang"],
        index=0,
    )

    st.sidebar.markdown("---")
    st.sidebar.info(
        "Model final: EfficientNetB0 Direct Multiclass\n\n"
        "Kelas: Healthy, Coccidiosis, Salmonella, Newcastle Disease"
    )

    if menu == "Beranda":
        show_home()
    elif menu == "Prediksi":
        show_prediction()
    elif menu == "Riwayat":
        show_history()
    elif menu == "Tentang":
        show_about()


if __name__ == "__main__":
    main()
