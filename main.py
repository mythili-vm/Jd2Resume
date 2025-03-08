from fastapi import FastAPI
from PyPDF2 import PdfReader

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Welcome to JD2Resume Parser!"}

@app.get("/resume")
async def read_resume():
    # Path to the PDF file
    pdf_path = "Mythili M resume.pdf"
    
    # Open the PDF file with PyPDF2
    reader = PdfReader(pdf_path)
    text = ""
    
    # Iterate through each page and extract text
    for page in reader.pages:
        text += page.extract_text()

    return {"content": text}