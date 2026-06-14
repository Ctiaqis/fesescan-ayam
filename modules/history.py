import streamlit as st

from utils.history_manager import clear_history, load_history


def show_history():
    st.title("Riwayat Prediksi")

    history_df = load_history()

    if history_df.empty:
        st.info("Belum ada riwayat prediksi.")
        return

    st.dataframe(history_df, use_container_width=True, hide_index=True)

    csv_data = history_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download Riwayat CSV",
        data=csv_data,
        file_name="prediction_history.csv",
        mime="text/csv",
    )

    if st.button("Hapus Riwayat", type="secondary"):
        clear_history()
        st.success("Riwayat berhasil dihapus.")
        st.rerun()
