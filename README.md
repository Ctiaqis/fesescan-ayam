# Screening Feses Ayam

Dashboard ini merupakan prototipe web untuk **screening awal penyakit ayam berbasis citra feses** menggunakan model **EfficientNetB0 Direct Multiclass**.

Model memprediksi gambar ke dalam empat kelas:

1. Healthy
2. Coccidiosis
3. Salmonella
4. Newcastle Disease

> Catatan: Dashboard ini hanya untuk screening awal, bukan diagnosis klinis.

## Struktur Project

```text
screening-feses-ayam/
│
├── dashboard.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
├── class_names.json
│
├── models/
│   └── efficientnetb0_direct_multiclass.keras
│
├── modules/
│   ├── home.py
│   ├── prediction.py
│   ├── history.py
│   └── about.py
│
├── utils/
│   ├── model_loader.py
│   ├── preprocessing.py
│   ├── gradcam.py
│   └── history_manager.py
│
├── assets/
└── data/
```

## Model

Masukkan file model hasil training ke folder `models/` dengan nama:

```text
efficientnetb0_direct_multiclass.keras
```

## Cara Menjalankan di Lokal

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run dashboard.py
```

Jika menggunakan Mac/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run dashboard.py
```

## File Penting

- `dashboard.py`: file utama untuk menjalankan web.
- `config.py`: konfigurasi path model, ukuran gambar, dan judul aplikasi.
- `class_names.json`: urutan nama kelas sesuai output model.
- `models/`: lokasi model `.keras`.
- `modules/`: halaman Beranda, Prediksi, Riwayat, dan Tentang.
- `utils/`: fungsi load model, preprocessing gambar, Grad-CAM, dan riwayat.

## Alur Prediksi

```text
Upload gambar feses ayam
        ↓
Preprocessing gambar 224×224
        ↓
EfficientNetB0 Direct Multiclass
        ↓
Prediksi kelas + confidence score
        ↓
Tampilan hasil dan Grad-CAM
```

## Alasan Model Dipilih

Model **EfficientNetB0 Direct Multiclass** dipilih karena memiliki recall tertinggi pada kelas minoritas **Newcastle Disease** dan tidak memiliki risiko error propagation. Hal ini lebih sesuai dengan tujuan sistem sebagai screening awal.
