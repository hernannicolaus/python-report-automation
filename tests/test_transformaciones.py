import pandas as pd

from src.transform import clean_and_cast, build_summaries, filtrar_por_fechas


def test_filtrar_por_fechas_sin_parametros_devuelve_todo():
    df = pd.DataFrame({
        "fecha": ["2025-11-01", "2025-12-01"],
        "categoria": ["Supermercado", "Transporte"],
        "descripcion": ["Compra", "Sube"],
        "medio_pago": ["Débito", "Saldo"],
        "monto": [1000, 500],
    })

    df = clean_and_cast(df)
    filtrado = filtrar_por_fechas(df, None, None)

    assert len(filtrado) == 2


def test_filtrar_por_fechas_rango_inclusive():
    df = pd.DataFrame({
        "fecha": ["2025-11-01", "2025-12-01", "2025-12-15", "2026-01-01"],
        "categoria": ["A", "B", "C", "D"],
        "descripcion": ["x", "y", "z", "w"],
        "medio_pago": ["Efectivo", "Tarjeta", "Tarjeta", "Débito"],
        "monto": [10, 20, 30, 40],
    })

    df = clean_and_cast(df)
    filtrado = filtrar_por_fechas(df, "2025-12-01", "2025-12-31")

    assert len(filtrado) == 2
    assert filtrado["fecha"].min() == pd.Timestamp("2025-12-01")
    assert filtrado["fecha"].max() == pd.Timestamp("2025-12-15")


def test_build_summaries_total_correcto():
    df = pd.DataFrame({
        "fecha": ["2025-11-01", "2025-11-02"],
        "categoria": ["A", "A"],
        "descripcion": ["x", "y"],
        "medio_pago": ["Efectivo", "Efectivo"],
        "monto": [100, 50],
    })

    df = clean_and_cast(df)
    total, por_mes, por_categoria, por_medio_pago, top_gastos = build_summaries(df)

    assert total == 150
