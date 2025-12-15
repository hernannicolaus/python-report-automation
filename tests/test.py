import pandas as pd
from src.transform import clean_and_cast, build_summaries

def test_build_summaries_total():
    df = pd.DataFrame({
        "fecha": ["2025-11-01", "2025-11-02"],
        "categoria": ["A", "A"],
        "descripcion": ["x", "y"],
        "monto": [10, 5],
    })

    df = clean_and_cast(df)
    total, por_mes, por_categoria = build_summaries(df)

    assert total == 15.0
    assert len(por_mes) == 1
    assert por_categoria.iloc[0]["monto"] == 15.0
