import json
from pathlib import Path
import streamlit as st
from openai import OpenAI
from config import OPENAI_API_KEY, NARRATIVE_MODEL, BASE_DIR

TEMPLATE_PATH = BASE_DIR / "data" / "narrative_templates.json"

def _load_fallback_template(pred_class: str) -> str:
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        templates = json.load(f)
    return templates.get(pred_class, "Deskripsi untuk kelas ini belum tersedia.")

@st.cache_data(show_spinner=False, ttl=3600)
def generate_narrative(pred_class: str, confidence: float, probabilities: dict) -> str:
    if not OPENAI_API_KEY:
        return _load_fallback_template(pred_class)

    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        prompt = f"""Kamu adalah asisten edukasi peternakan ayam.
Berdasarkan hasil klasifikasi model AI berikut, buat narasi singkat (maks 4 kalimat, bahasa Indonesia awam):

Kelas terdeteksi: {pred_class}
Confidence: {confidence*100:.1f}%

Aturan:
- Jelaskan apa arti kelas ini secara umum (ciri feses, kemungkinan penyebab umum).
- JANGAN memberi dosis obat atau instruksi pengobatan spesifik.
- Akhiri dengan anjuran konsultasi ke dokter hewan/PPL setempat untuk kepastian.
- Jangan gunakan format markdown, tulis sebagai paragraf biasa."""

        response = client.chat.completions.create(
            model=NARRATIVE_MODEL,
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip()

    except Exception:
        return _load_fallback_template(pred_class)