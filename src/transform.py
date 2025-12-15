import pandas as pd

def clean_and_cast(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliza tipos y valida datos mínimos.
    Espera columnas: fecha, categoria, descripcion, monto
    """
    out = df.copy()

    out["fecha"] = pd.to_datetime(out["fecha"], errors="raise")
    out["monto"] = pd.to_numeric(out["monto"], errors="raise")
    out["categoria"] = out["categoria"].astype(str).str.strip()
    out["descripcion"] = out["descripcion"].astype(str).str.strip()
    out["medio_pago"] = out["medio_pago"].astype(str).str.strip()

    if out["monto"].isna().any():
        raise ValueError("Hay montos nulos luego de convertir a numérico.")
    return out

def build_summaries(df: pd.DataFrame):
    tmp = df.copy()
    tmp["mes"] = tmp["fecha"].dt.to_period("M").astype(str)

    por_mes = (
        tmp.groupby("mes", as_index=False)["monto"]
        .sum()
        .sort_values("mes")
        .reset_index(drop=True)
    )

    por_categoria = (
        tmp.groupby("categoria", as_index=False)["monto"]
        .sum()
        .sort_values("monto", ascending=False)
        .reset_index(drop=True)
    )

    por_medio_pago = (
        tmp.groupby("medio_pago", as_index=False)["monto"]
        .sum()
        .sort_values("monto", ascending=False)
        .reset_index(drop=True)
    )

    top_gastos = (
        tmp.sort_values("monto", ascending=False)
        .head(10)
        .reset_index(drop=True)
    )

    total = float(tmp["monto"].sum())
    return total, por_mes, por_categoria, por_medio_pago, top_gastos
