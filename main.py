import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
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
    pdf.ln(8)

    # Reads Excel file
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    column = [items.replace("_", " ").title() for items in df.columns]

    # Add header
    pdf.cell(w=30, h=6, txt=column[0], border=1)
    pdf.cell(w=50, h=6, txt=column[1], border=1)
    pdf.cell(w=50, h=6, txt=column[2], border=1)
    pdf.cell(w=30, h=6, txt=column[3], border=1)
    pdf.cell(w=30, h=6, txt=column[4], border=1,ln=1)

    # Add rows to table
    for index,row in df.iterrows():
        pdf.set_font('Times',size=10)
        pdf.set_text_color(100,100,100)
        pdf.cell(w=30, h=6 ,txt=str(row["product_id"]),border=1)
        pdf.cell(w=50, h=6, txt=str(row["product_name"]), border=1)
        pdf.cell(w=50, h=6, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=6, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=6, txt=str(row["total_price"]), border=1,ln=1)

    sum= df["total_price"].sum()
    pdf.set_font('Times', size=10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=30, h=6, txt=" ", border=1)
    pdf.cell(w=50, h=6, txt=" ", border=1)
    pdf.cell(w=50, h=6, txt=" ", border=1)
    pdf.cell(w=30, h=6, txt=" ", border=1)
    pdf.cell(w=30, h=6, txt=str(sum), border=1, ln=1)

    pdf.ln(5)
    # Total sum sentence
    pdf.set_font('Times', size=12)
    pdf.set_text_color(0,0,0)
    pdf.cell(w=50, h=6, txt=f"The total price is {sum}.",ln=1)
    pdf.ln(2)

    # company name and logo
    pdf.set_font('Times', size=12, style='B')
    pdf.set_text_color(0,0,0)
    pdf.cell(w=23, h=6, txt="PythonHow", ln=0)
    pdf.image("pythonhow.png", w=10, h=10)

    # output
    pdf.output(f"invoices_PDF/invoices{invoice_nr}.pdf")