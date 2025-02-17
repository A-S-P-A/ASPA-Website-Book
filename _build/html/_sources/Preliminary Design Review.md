# Preliminary Design Review

```python
import fitz  # PyMuPDF

pdf_path = "Preliminary Design Review.pdf"
doc = fitz.open(Preliminary Design Review)

for page in doc:
    text = page.get_text("text")
    print(text)  # Print text from each page
```
