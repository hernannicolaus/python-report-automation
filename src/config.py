from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

INPUT_DIR = ROOT_DIR / "input"
OUTPUT_DIR = ROOT_DIR / "output"
LOG_DIR = ROOT_DIR / "logs"

DEFAULT_INPUT_FILE = INPUT_DIR / "ventas.csv"
DEFAULT_EXCEL_OUT = OUTPUT_DIR / "reporte.xlsx"
DEFAULT_PDF_OUT = OUTPUT_DIR / "reporte.pdf"
DEFAULT_LOG_FILE = LOG_DIR / "app.log"
