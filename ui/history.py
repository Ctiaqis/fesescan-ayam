import streamlit as st

from utils.history_manager import clear_history, load_history


def show_history():
    st.markdown("<h1 style='margin-bottom:4px;'>📋 Riwayat Prediksi</h1>",
                unsafe_allow_html=True)
    st.markdown(
        "<p style='margin-bottom:24px;'>"
        "Data hasil prediksi yang telah dilakukan sebelumnya."
        "</p>",
        unsafe_allow_html=True,
    )

    history_df = load_history()

    # ── Action Bar ────────────────────────────────────────────────────────────
    with st.container(border=True):
        info_col, btn_col = st.columns([2, 1])

        with info_col:
            total = len(history_df) if not history_df.empty else 0
            st.metric("Total Prediksi", total, label_visibility="visible")

        with btn_col:
            b1, b2 = st.columns(2, gap="small")
            with b1:
                if not history_df.empty:
                    csv_data = history_df.to_csv(index=False).encode("utf-8")
                    st.download_button(
                        "⬇️ CSV",
                        data=csv_data,
                        file_name="prediction_history.csv",
                        mime="text/csv",
                        use_container_width=True,
                    )
                else:
                    st.button("⬇️ CSV", disabled=True, use_container_width=True)

            with b2:
                if st.button(
                    "🗑️ Hapus",
                    type="secondary",
                    use_container_width=True,
                    disabled=history_df.empty,
                ):
                    clear_history()
                    st.success("Riwayat berhasil dihapus.")
                    st.rerun()

    # ── Tabel Riwayat ─────────────────────────────────────────────────────────
    with st.container(border=True):
        if history_df.empty:
            st.markdown("""
            <div style="text-align:center; padding:48px 0;">
                <div style="font-size:40px; margin-bottom:12px;">📭</div>
                <div style="font-size:15px; font-weight:600; color:#1F1B2E;
                            margin-bottom:6px;">Belum Ada Riwayat</div>
                <p style="font-size:13px; margin:0;">
                    Lakukan prediksi pertama Anda di menu <strong>Prediksi</strong>.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Rename kolom agar lebih rapi
            display_df = history_df.copy()
            rename_map = {
                "waktu": "Tanggal & Waktu",
                "nama_file": "Nama File",
                "prediksi": "Hasil Prediksi",
                "confidence": "Confidence (%)",
            }
            display_df.rename(
                columns={k: v for k, v in rename_map.items() if k in display_df.columns},
                inplace=True,
            )

            st.dataframe(
                display_df,
                use_container_width=True,
                hide_index=True,
                height=460,
            )