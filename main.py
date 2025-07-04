from fastapi import FastAPI, UploadFile, Form, File
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

app = FastAPI()

# Allow frontend (optional for local testing or external UI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve index.html as frontend UI
@app.get("/", response_class=FileResponse)
def serve_ui():
    return "index.html"

# Mount current folder as static (for index.html, CSS, etc.)
app.mount("/static", StaticFiles(directory="."), name="static")

@app.post("/analyze-resume/")
async def analyze_resume(file: UploadFile = File(...), job_description: str = Form(...)):
    try:
        # Read PDF resume text
        contents = await file.read()
        with open("temp_resume.pdf", "wb") as f:
            f.write(contents)

        reader = PdfReader("temp_resume.pdf")
        resume_text = ""
        for page in reader.pages:
            resume_text += page.extract_text() or ""

        # TF-IDF similarity
        documents = [resume_text, job_description]
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(documents)
        score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0] * 100

        verdict = "✅ Strong match!" if score >= 75 else "⚠️ Moderate/low match"

        return JSONResponse({
            "match_percentage": score,
            "verdict": verdict
        })

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
