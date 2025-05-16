import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    # Reads Excel file
    df = pd.read_excel(filepath , sheet_name= "Sheet 1")

    # PDF created
    pdf = FPDF( orientation = 'P', unit= 'mm' , format = 'A4')
    pdf.add_page()

    # Invoice number and date
    paths= Path(filepath).stem
    invoice_nr,date= paths.split("-")

    # fonts and cells
    pdf.set_font('Times', 'B', 12)
    pdf.cell(w=50,h= 8,txt=f'Invoice nr: {invoice_nr}',border=0,ln=1,align="L")
    pdf.set_font('Times', 'B', 12)
    pdf.cell(w=50,h= 8,txt=f'Date: {date}',border=0,ln=1,align="L")


    # output
    pdf.output(f"invoices_PDF/invoices{invoice_nr}.pdf")