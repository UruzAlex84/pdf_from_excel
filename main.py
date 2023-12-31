import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob(r"invoices\\*.xlsx")

for filepath in filepaths:

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem

    # Get number and date from filename
    invoice_nr, date = filename.split("-")

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)
    pdf.ln(6)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # Add a header
    columns = df.columns
    # Replace underscore sign
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family="Times", size=10, style='B')
    pdf.set_text_color(60, 60, 60)
    pdf.cell(w=30, h=8, txt=columns[0], border=1, align='C')
    pdf.cell(w=70, h=8, txt=columns[1], border=1, align='C')
    pdf.cell(w=30, h=8, txt=columns[2], border=1, align='C')
    pdf.cell(w=30, h=8, txt=columns[3], border=1, align='C')
    pdf.cell(w=30, h=8, txt=columns[4], border=1, align='C', ln=1)

    # Add rows to the table
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1, align='C')
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1, align='C')
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1, align='C')
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, align='C', ln=1)

    sum_price = df["total_price"].sum()
    pdf.set_font(family="Times", size=10, style='B')
    pdf.set_text_color(60, 60, 60)
    pdf.cell(w=30, h=8, txt="", border=1, align='C')
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1, align='C')
    pdf.cell(w=30, h=8, txt="", border=1, align='C')
    pdf.cell(w=30, h=8, txt=str(sum_price), border=1, align='C', ln=1)

    pdf.ln(6)
    # Add total sum and company name with logo
    pdf.set_font(family="Times", size=14, style="B")
    pdf.cell(w=70, h=8, txt=f"The total price is {sum_price}", ln=1)
    pdf.cell(w=40, h=10, txt="Horn and Hoofs")
    pdf.image("pythonhow.png", w=10)

    pdf.output(fr"PDFs\\{filename}.pdf")
