import argparse
from pathlib import Path

from config import (
    DEFAULT_INPUT_FILE,
    DEFAULT_EXCEL_OUT,
    DEFAULT_PDF_OUT,
    DEFAULT_LOG_FILE,
)
from logger import setup_logger
from ioUtils import read_input
from transform import clean_and_cast, build_summaries
from reportExcel import export_excel
from reportPdf import export_pdf


def parse_args():
    parser = argparse.ArgumentParser(
        description="Automatizador de reportes de gastos personales (Excel + PDF)"
    )
    parser.add_argument(
        "--input",
        type=str,
        default=str(DEFAULT_INPUT_FILE),
        help="Ruta del archivo de entrada (.csv o .xlsx)",
    )
    parser.add_argument(
        "--excel",
        type=str,
        default=str(DEFAULT_EXCEL_OUT),
        help="Ruta de salida del Excel",
    )
    parser.add_argument(
        "--pdf",
        type=str,
        default=str(DEFAULT_PDF_OUT),
        help="Ruta de salida del PDF",
    )
    parser.add_argument(
        "--log",
        type=str,
        default=str(DEFAULT_LOG_FILE),
        help="Ruta del archivo de log",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    logger = setup_logger(Path(args.log))
    logger.info("Iniciando generación de reportes de gastos personales")

    try:
        input_path = Path(args.input)
        excel_out = Path(args.excel)
        pdf_out = Path(args.pdf)

        df_raw = read_input(input_path)
        logger.info(f"Archivo leído: {input_path} | filas={len(df_raw)}")

        df = clean_and_cast(df_raw)

        total, por_mes, por_categoria, por_medio_pago, top_gastos = build_summaries(df)

        export_excel(
            total,
            por_mes,
            por_categoria,
            por_medio_pago,
            top_gastos,
            excel_out,
        )
        logger.info(f"Excel generado: {excel_out}")

        export_pdf(
            total,
            por_mes,
            por_categoria,
            por_medio_pago,
            pdf_out,
        )
        logger.info(f"PDF generado: {pdf_out}")

        logger.info("Proceso finalizado correctamente")
        print("OK ✅")
        print(f"- Excel: {excel_out}")
        print(f"- PDF:   {pdf_out}")

    except Exception as e:
        logger.exception("Error durante la generación de reportes")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
