# Styling shadcn/ui untuk Streamlit — DARK MODE navy + accent gold/amber, logo ayam emas

SHADCN_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --foreground: #e2e8f0;
    --muted-foreground: #94a3b8;
    --surface: #111827;
    --surface-2: #1e293b;
    --border: #1e293b;
    --border-strong: #334155;
    --primary: #f59e0b;
    --primary-hover: #d97706;
    --primary-foreground: #1f2937;
    --radius: 0.75rem;
    --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.4);
    --shadow: 0 2px 6px -1px rgb(0 0 0 / 0.5);
    --shadow-lg: 0 18px 40px -16px rgb(0 0 0 / 0.7);
}

html, body, .stApp {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

/* Background halaman: navy gelap dengan glow indigo lembut */
.stApp {
    background:
        radial-gradient(800px 500px at 12% -5%, #1e3a8a 0%, rgba(30,58,138,0) 55%),
        radial-gradient(800px 500px at 90% 105%, #312e81 0%, rgba(49,46,129,0) 55%),
        #0b1120;
}

/* Kontainer utama jadi satu panel/bingkai melayang */
.block-container {
    max-width: 760px;
    background: #0f172a;
    border: 1px solid var(--border);
    border-radius: 1.5rem;
    box-shadow: var(--shadow-lg);
    padding: 2rem 2.25rem 2.5rem !important;
    margin-top: 2.5rem;
    margin-bottom: 3rem;
}

/* ===== HERO ===== */
.hero {
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 55%, #1e3a8a 100%);
    border: 1px solid var(--border-strong);
    border-radius: 1.25rem;
    padding: 1.75rem 1.9rem;
    color: #fff;
    box-shadow: var(--shadow-lg);
    position: relative;
    overflow: hidden;
    margin-bottom: 1.75rem;
}
.hero::after {
    content: "";
    position: absolute;
    right: -50px; top: -50px;
    width: 220px; height: 220px;
    background: radial-gradient(circle, rgba(245,158,11,0.18) 0%, rgba(245,158,11,0) 70%);
}
.hero-row {
    display: flex;
    align-items: center;
    gap: 1.1rem;
    position: relative;
    z-index: 1;
}
.logo {
    flex: 0 0 auto;
    width: 64px; height: 64px;
    border-radius: 1rem;
    background: linear-gradient(160deg, #fde68a 0%, #f59e0b 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2.1rem;
    box-shadow: 0 8px 20px -6px rgb(245 158 11 / 0.6), inset 0 1px 0 rgb(255 255 255 / 0.5);
    border: 1px solid rgba(255,255,255,0.35);
}
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: rgba(245,158,11,0.14);
    border: 1px solid rgba(245,158,11,0.35);
    color: #fcd34d;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.03em;
    padding: 0.25rem 0.65rem;
    border-radius: 9999px;
    margin-bottom: 0.55rem;
}
.hero-title {
    font-size: 1.55rem;
    font-weight: 800;
    line-height: 1.2;
    letter-spacing: -0.025em;
    color: #f8fafc;
    margin: 0 0 0.3rem 0;
}
.hero-sub {
    font-size: 0.88rem;
    color: #cbd5e1;
    margin: 0;
    font-weight: 400;
}

/* ===== SECTION LABEL ===== */
.section-label {
    font-size: 0.95rem;
    font-weight: 600;
    color: var(--foreground);
    letter-spacing: -0.01em;
    margin: 1.25rem 0 0.6rem 0;
    display: flex;
    align-items: center;
    gap: 0.45rem;
}

h1, h2, h3 { color: var(--foreground) !important; }
h1 { font-size: 1.5rem !important; font-weight: 700 !important; letter-spacing: -0.02em !important; }
h2 { font-size: 1.15rem !important; font-weight: 600 !important; }
h3 { font-size: 1rem !important; font-weight: 600 !important; }

label, .stFileUploader label p {
    font-size: 0.875rem !important;
    font-weight: 500 !important;
    color: var(--foreground) !important;
}

/* ===== TOMBOL ===== */
.stButton > button, .stDownloadButton > button {
    border-radius: var(--radius) !important;
    border: 1px solid var(--border-strong) !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    padding: 0.6rem 1rem !important;
    box-shadow: var(--shadow-sm) !important;
    transition: all 0.15s ease !important;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #f59e0b, #d97706) !important;
    color: var(--primary-foreground) !important;
    border-color: transparent !important;
}
.stButton > button[kind="primary"]:hover {
    box-shadow: 0 8px 22px -8px rgb(245 158 11 / 0.7) !important;
    transform: translateY(-1px);
}
.stButton > button[kind="secondary"] {
    background: var(--surface-2) !important;
    color: var(--foreground) !important;
}
.stButton > button[kind="secondary"]:hover {
    background: #273449 !important;
    border-color: #475569 !important;
}

/* ===== FILE UPLOADER ===== */
[data-testid="stFileUploaderDropzone"] {
    border: 1.5px dashed var(--border-strong) !important;
    border-radius: var(--radius) !important;
    background: var(--surface) !important;
    padding: 1.5rem !important;
    transition: border-color 0.15s ease, background 0.15s ease !important;
}
[data-testid="stFileUploaderDropzone"]:hover {
    border-color: var(--primary) !important;
    background: #15203a !important;
}
[data-testid="stFileUploaderDropzoneInstructions"] span,
[data-testid="stFileUploaderDropzoneInstructions"] small {
    color: var(--muted-foreground) !important;
}
[data-testid="stFileUploaderDropzone"] button {
    background: var(--surface-2) !important;
    color: var(--foreground) !important;
    border: 1px solid var(--border-strong) !important;
    border-radius: var(--radius) !important;
    font-weight: 600 !important;
}
[data-testid="stFileUploaderDropzone"] button:hover {
    background: #273449 !important;
    border-color: #475569 !important;
}

/* ===== METRIC CARD ===== */
[data-testid="stMetric"] {
    background: var(--surface);
    border: 1px solid var(--border-strong);
    border-radius: var(--radius);
    padding: 1.1rem 1.25rem;
    box-shadow: var(--shadow);
}
[data-testid="stMetricLabel"] p {
    color: var(--muted-foreground) !important;
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}
[data-testid="stMetricValue"] {
    color: #fcd34d !important;
    font-weight: 800 !important;
    font-size: 1.6rem !important;
    letter-spacing: -0.02em;
}

/* ===== GAMBAR ===== */
[data-testid="stImage"] img {
    object-fit: contain !important;
    border-radius: var(--radius) !important;
    border: 1px solid var(--border-strong) !important;
    box-shadow: var(--shadow) !important;
}
[data-testid="stImage"] figcaption {
    color: var(--muted-foreground) !important;
    font-size: 0.8rem !important;
}

/* ===== PROBABILITAS (custom bar) ===== */
.prob-row { margin: 0.55rem 0 0.85rem 0; }
.prob-head {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 0.35rem;
}
.prob-name { font-size: 0.88rem; font-weight: 500; color: var(--foreground); }
.prob-name.top { font-weight: 700; color: #fcd34d; }
.prob-val { font-size: 0.82rem; font-weight: 600; color: var(--muted-foreground); font-variant-numeric: tabular-nums; }
.prob-val.top { color: #fcd34d; }
.prob-track {
    width: 100%;
    height: 0.5rem;
    background: var(--surface-2);
    border-radius: 9999px;
    overflow: hidden;
}
.prob-fill {
    height: 100%;
    background: #475569;
    border-radius: 9999px;
    transition: width 0.4s ease;
}
.prob-fill.top {
    background: linear-gradient(90deg, #f59e0b, #fbbf24);
}

/* ===== ALERT ===== */
[data-testid="stAlert"] {
    border-radius: var(--radius) !important;
    border: 1px solid var(--border-strong) !important;
    background: var(--surface) !important;
    box-shadow: var(--shadow-sm) !important;
}
[data-testid="stAlert"] > div { background: transparent !important; }
[data-testid="stAlert"] p, [data-testid="stAlert"] div, [data-testid="stAlert"] span {
    color: #cbd5e1 !important;
    font-size: 0.85rem !important;
}

hr { border-color: var(--border) !important; margin: 1.5rem 0 !important; }

.stSpinner > div { color: var(--muted-foreground) !important; }

/* Footer disclaimer kustom */
.disclaimer {
    display: flex;
    gap: 0.6rem;
    align-items: flex-start;
    background: var(--surface);
    border: 1px solid var(--border-strong);
    border-radius: var(--radius);
    padding: 0.9rem 1.1rem;
    color: var(--muted-foreground);
    font-size: 0.82rem;
    line-height: 1.5;
    margin-top: 0.5rem;
}
.disclaimer .ico { font-size: 1rem; line-height: 1.4; }

#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
[data-testid="stHeader"] { background: transparent; }

/* ============================================================
   DESKTOP LAYOUT
   ============================================================ */
.block-container,
div[data-testid="stAppViewBlockContainer"] {
    max-width: 1200px;
    margin: 0 auto;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

div[data-testid="stHorizontalBlock"] {
    gap: 2rem;
    align-items: flex-start;
}

.empty-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 0.75rem;
    padding: 3.5rem 1.5rem;
    border: 1.5px dashed rgba(148, 163, 184, 0.35);
    border-radius: 14px;
    text-align: center;
    min-height: 220px;
}
.empty-state-icon { font-size: 2rem; opacity: 0.6; }
.empty-state-text { font-size: 0.9rem; opacity: 0.65; max-width: 260px; }

.narrative-box {
    padding: 1rem 1.25rem;
    border-radius: 12px;
    border: 1px solid rgba(148, 163, 184, 0.25);
    line-height: 1.6;
    font-size: 0.92rem;
    margin-bottom: 0.5rem;
}

/* ============================================================
   RESPONSIVE — kembali ke 1 kolom di layar sempit
   ============================================================ */
@media (max-width: 900px) {
    .block-container,
    div[data-testid="stAppViewBlockContainer"] {
        max-width: 100%;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    div[data-testid="stHorizontalBlock"] {
        flex-direction: column !important;
    }
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"],
    div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {
        width: 100% !important;
        flex: 1 1 100% !important;
    }
}
</style>


"""
