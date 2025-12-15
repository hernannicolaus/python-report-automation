## 🚀 Personal Expenses Report Automation (Python)

Python project that automates personal expenses reporting.
It reads CSV/XLSX input files, processes and summarizes data, and generates:

- 📊 Excel report (multiple sheets)
- 📄 PDF summary report
- 🧾 Application logs

### Features
- Monthly expenses summary
- Expenses by category and payment method
- Top 10 highest expenses
- CLI parameters
- Logging and error handling

### Tech Stack
- Python 3
- pandas
- openpyxl
- reportlab

### How to run
```bash
pip install -r requirements.txt
python src/main.py

### Ejecutar tests
python -m pytest
