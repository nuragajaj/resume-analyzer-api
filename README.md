# 📄 Resume Analyzer API

A FastAPI-powered microservice that analyzes resumes against job descriptions and returns a match percentage — helping recruiters, HR teams, and applicants quickly evaluate job-fit.

---

## 🚀 Features

- 📂 Upload resume in PDF format
- 📄 Paste any job description
- 🔍 Get a match percentage based on keyword relevance (TF-IDF + Cosine Similarity)
- ⚡ Built using FastAPI, PyPDF2, and Scikit-learn
- 🌐 Interactive API docs via Swagger (`/docs`)

---

## 🛠️ Tech Stack

| Technology      | Purpose                          |
|-----------------|----------------------------------|
| FastAPI         | Web framework for REST API       |
| PyPDF2          | Extract text from PDF resumes    |
| scikit-learn    | TF-IDF vectorization & similarity|
| Uvicorn         | ASGI server to run the API       |
| VS Code         | Code editor                      |

---

## 📦 Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
## 🌐 Live Demo

Try the live Resume Analyzer API here:  
👉 [https://resume-analyzer-api-x206.onrender.com/docs](https://resume-analyzer-api-x206.onrender.com/docs)
