import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath , sheet_name= "Sheet 1")
    pdf = FPDF( orientation = 'P', unit= 'mm' , format = 'A4')
    pdf.add_page()
    pdf.set_font('Times', 'B', 12)
    paths= Path(filepath).stem
    invoice_nr= paths.split("-")[0]
    pdf.cell(w=50,h= 17,txt=f'Invoice nr.{invoice_nr}',border=0,ln=1,align="L")
    pdf.output(f"invoices_PDF/invoices{invoice_nr}.pdf")