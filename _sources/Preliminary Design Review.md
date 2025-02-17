# Preliminary Design Review

```python
import fitz  # PyMuPDF

pdf_path = "Preliminary Design Review.pdf"
doc = fitz.open(pdf_path)

for page in doc:
    text = page.get_text("text")
    print(text)  # Print text from each page
```
```python
import os

pdf_path = "Preliminary Design Review.pdf"
print("File exists:", os.path.exists(pdf_path))
```