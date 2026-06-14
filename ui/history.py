import streamlit as st
import pandas as pd

from utils.history_manager import clear_history, load_history

def show_history():
    st.markdown("<h1 style='margin-bottom: 8px;'>Riwayat Prediksi</h1>", unsafe_allow_html=True)
    st.markdown("<p style='margin-bottom: 24px;'>Kelola data hasil prediksi yang telah dilakukan sebelumnya.</p>", unsafe_allow_html=True)

    history_df = load_history()

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col3:
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if not history_df.empty:
                csv_data = history_df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    "Download CSV",
                    data=csv_data,
                    file_name="prediction_history.csv",
                    mime="text/csv",
                    use_container_width=True
                )
        with btn_col2:
            if st.button("Hapus Riwayat", type="secondary", use_container_width=True):
                clear_history()
                st.success("Riwayat berhasil dihapus.")
                st.rerun()
                
    st.markdown("<hr style='margin: 16px 0; border: none; border-top: 1px solid #E5E7EB;'/>", unsafe_allow_html=True)

    if history_df.empty:
        st.info("Belum ada riwayat prediksi.")
    else:
        st.dataframe(
            history_df,
            use_container_width=True,
            hide_index=True,
            height=500
        )
        
    st.markdown("</div>", unsafe_allow_html=True)
