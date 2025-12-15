from pathlib import Path
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def export_pdf(total: float, por_mes: pd.DataFrame, por_categoria: pd.DataFrame,
               por_medio_pago: pd.DataFrame, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(out_path), pagesize=A4)
    width, height = A4

    y = height - 60
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Reporte de gastos personales")
    y -= 30

    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Total gastado: ${total:,.2f}")
    y -= 25

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Gasto por mes:")
    y -= 18
    c.setFont("Helvetica", 11)
    for _, row in por_mes.iterrows():
        c.drawString(60, y, f"{row['mes']}: ${row['monto']:,.2f}")
        y -= 14

    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Top categorías:")
    y -= 18
    c.setFont("Helvetica", 11)
    for _, row in por_categoria.head(5).iterrows():
        c.drawString(60, y, f"{row['categoria']}: ${row['monto']:,.2f}")
        y -= 14

    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Medios de pago:")
    y -= 18
    c.setFont("Helvetica", 11)
    for _, row in por_medio_pago.iterrows():
        c.drawString(60, y, f"{row['medio_pago']}: ${row['monto']:,.2f}")
        y -= 14
        if y < 80:
            c.showPage()
            y = height - 60

    c.save()
