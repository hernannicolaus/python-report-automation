from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = {"fecha", "categoria", "descripcion", "monto", "medio_pago"}


def read_input(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"No existe el archivo de entrada: {path}")

    if path.suffix.lower() == ".csv":
        df = pd.read_csv(path)
    elif path.suffix.lower() in {".xlsx", ".xls"}:
        df = pd.read_excel(path)
    else:
        raise ValueError("Formato no soportado. Usá .csv o .xlsx")

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas requeridas: {sorted(missing)}")

    return df

def ensure_output_dir(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
