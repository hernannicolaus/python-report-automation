from pathlib import Path
import pandas as pd

def export_excel(total: float, por_mes: pd.DataFrame, por_categoria: pd.DataFrame,
                 por_medio_pago: pd.DataFrame, top_gastos: pd.DataFrame, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with pd.ExcelWriter(out_path, engine="openpyxl") as writer:
        pd.DataFrame({"total": [total]}).to_excel(writer, index=False, sheet_name="resumen")
        por_mes.to_excel(writer, index=False, sheet_name="por_mes")
        por_categoria.to_excel(writer, index=False, sheet_name="por_categoria")
        por_medio_pago.to_excel(writer, index=False, sheet_name="por_medio_pago")
        top_gastos.to_excel(writer, index=False, sheet_name="top_10_gastos")
