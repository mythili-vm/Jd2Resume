from fastapi import FastAPI
from PyPDF2 import PdfReader
from genai import get_ai_response

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Welcome to JD2Resume Parser!"}

@app.get("/resume")
async def read_resume():
    # Path to the PDF file
    resume = parser("resume.pdf")
    jd = parser("testEngineer.pdf")

    return {get_ai_response("you are an expert resume analyser and jd matcher.",
                                       f"Modify the following resume to fit the job description as json object and list the skills that are missing as a separate jsonKey:\nResume:{resume}\n\nJob Description:\n{jd}")}

def parser(pdf_path):
    # Open the PDF file with PyPDF2
    reader = PdfReader(pdf_path)
    text = ""
    print("parsing ",pdf_path)
    # Iterate through each page and extract text
    for page in reader.pages:
        text += page.extract_text()

    return text