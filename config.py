# judul aplikasi, path model, ukuran gambar

from pathlib import Path

# ============================================================
# KONFIGURASI UTAMA
# ============================================================
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPEN_AI_KEY")
NARRATIVE_MODEL = "gpt-4o-mini"  # murah, cepat, cukup untuk narasi pendek


# test cepat, bisa taruh di akhir config.py sementara lalu hapus lagi
print("API KEY loaded:", bool(OPENAI_API_KEY))

BASE_DIR = Path(__file__).resolve().parent

APP_TITLE = "Screening Awal Penyakit Ayam Berbasis Citra Feses"
APP_SUBTITLE = "EfficientNetB0 Direct Multiclass"

MODEL_PATH = BASE_DIR / "models" / "efficientnetb0_direct_multiclass.keras"
CLASS_NAMES_PATH = BASE_DIR / "class_names.json"
HISTORY_PATH = BASE_DIR / "data" / "prediction_history.csv"

IMG_SIZE = (224, 224)

ALLOWED_EXTENSIONS = ["jpg", "jpeg", "png"]

DISCLAIMER = (
    "Sistem ini hanya digunakan untuk screening awal dan bukan sebagai diagnosis klinis. "
    "Hasil prediksi tetap perlu dikonfirmasi oleh ahli atau pemeriksaan lanjutan."
)
