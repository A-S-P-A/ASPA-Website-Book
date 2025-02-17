#import os

#pdf_path = "Preliminary Design Review.pdf"
#print("File exists:", os.path.exists(pdf_path))

#import fitz  # PyMuPDF

#pdf_path = "Preliminary Design Review.pdf"
#doc = fitz.open(pdf_path)

#for page in doc:
#    text = page.get_text("text")
 #   print(text)  # Print text from each page

from pdf2image import convert_from_path

pdf_path = "Structural Front End Report.pdf"
images = convert_from_path(pdf_path)

for i, image in enumerate(images):
    image.save(f"page_{i+1}.png", "PNG")
