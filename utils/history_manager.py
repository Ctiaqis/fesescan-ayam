from pathlib import Path

import pandas as pd

from config import HISTORY_PATH


COLUMNS = ["waktu", "nama_file", "prediksi", "confidence"]


def ensure_history_file():
    history_path = Path(HISTORY_PATH)
    history_path.parent.mkdir(parents=True, exist_ok=True)

    if not history_path.exists():
        pd.DataFrame(columns=COLUMNS).to_csv(history_path, index=False)


def save_history(item: dict):
    ensure_history_file()
    history_path = Path(HISTORY_PATH)

    history_df = pd.read_csv(history_path)
    new_df = pd.DataFrame([item])
    history_df = pd.concat([history_df, new_df], ignore_index=True)
    history_df.to_csv(history_path, index=False)


def load_history():
    ensure_history_file()
    return pd.read_csv(HISTORY_PATH)


def clear_history():
    Path(HISTORY_PATH).parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(columns=COLUMNS).to_csv(HISTORY_PATH, index=False)
