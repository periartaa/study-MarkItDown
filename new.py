import os
import pdfplumber
import docx
import openpyxl
from pptx import Presentation

def read_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    content = ""

    if ext == ".pdf":
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                content += page.extract_text() + "\n"

    elif ext == ".docx":
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            content += para.text + "\n"

    elif ext == ".pptx":
        prs = Presentation(file_path)
        for slide in prs.slides:
            for shape in slide.shapes:
                if hasattr(shape, "text"):
                    content += shape.text + "\n"

    elif ext == ".xlsx":
        wb = openpyxl.load_workbook(file_path)
        for sheet in wb.worksheets:
            content += f"# {sheet.title}\n"
            for row in sheet.iter_rows(values_only=True):
                content += ' | '.join([str(cell) if cell is not None else "" for cell in row]) + "\n"

    else:
        content = "Format file tidak didukung."

    return content

# Contoh penggunaan
# file_path = "Book1.xlsx"  # Bisa ganti dengan file .pdf, .docx, .pptx
file_path = "study-MarkItDown\word.pdf"  # Ganti dengan path file yang ingin dibaca
print(read_file(file_path))
