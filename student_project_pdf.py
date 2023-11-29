import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob(r"text_files\\*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf_name = "student_project"
for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem
    name = filename.title()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{name}")
pdf.output(fr"PDFs\{pdf_name}.pdf")
