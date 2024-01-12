import pdfplumber

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

# 使用示例
pdf_path = './111.pdf'
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)

