from fastapi import FastAPI, File, UploadFile, Form
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "👋 Welcome to the Resume Analyzer API! Upload your resume and get a match score against a job description."}


@app.post("/analyze-resume/")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    #Save the uploaded PDF temporarily
    file_location = "temp_resume.pdf"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    #Extract text from resume
    try:
        reader = PdfReader(file_location)
        resume_text = "".join([page.extract_text() or "" for page in reader.pages])
    except:
        return {"error": "❌ Failed to read the PDF. Please upload a valid resume."}
    finally:
        os.remove(file_location)  # cleanup

    #Use TF-IDF to compare resume and JD
    documents = [resume_text, job_description]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)

    similarity_score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0] * 100

    result = {
        "match_percentage": round(similarity_score, 2),
        "verdict": "✅ Strong match!" if similarity_score > 60 else "⚠️ Could be improved."
    }

    return result
