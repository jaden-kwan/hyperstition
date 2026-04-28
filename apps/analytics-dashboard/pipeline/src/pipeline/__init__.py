from pathlib import Path

PIPELINE_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PIPELINE_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
CODED_DIR = DATA_DIR / "coded"
DB_PATH = DATA_DIR / "posts.db"
PROMPTS_DIR = PIPELINE_ROOT / "prompts"

for _d in (RAW_DIR, CODED_DIR):
    _d.mkdir(parents=True, exist_ok=True)
