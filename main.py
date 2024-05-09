from PyPDF2 import PdfReader
from PIL import Image
from tqdm import tqdm

import pytesseract
import fitz
import os

os.environ["TESSDATA_PREFIX"] = "./traineddata"

def extract_text_from_pdf(pdf_path):
    final_text = ""

    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)

        for page_number, page in tqdm(enumerate(reader.pages)):
            text = page.extract_text()

            if not text.strip():
                document = fitz.open(pdf_path)
                pdf_page = document[page_number]
                pixmap = pdf_page.get_pixmap(matrix=fitz.Matrix(3, 3))

                img = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
                ocr_text = pytesseract.image_to_string(img, lang='fra')
                final_text += ocr_text
            else:
                print(f"Page {page_number + 1} is extracted using PyPDF2")
                final_text += text

    return final_text

if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ")

    extracted_text = extract_text_from_pdf(pdf_path)
    with open("result.txt", "w", encoding="utf-8") as file:
        file.write(extracted_text)
