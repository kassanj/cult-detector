"""
Simple FastAPI server for the cult detector.
Takes a description, returns a JSON analysis.
No streaming — straightforward request/response.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from chain import analyze

app = FastAPI(
    title="Is This a Cult?",
    description="Deadpan RAG-powered cult likelihood analyzer",
    version="1.0.0"
)

# Allow frontend or Postman to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── REQUEST SCHEMA ────────────────────────────────────────────────
class AnalysisRequest(BaseModel):
    description: str


# ── ROUTES ───────────────────────────────────────────────────────
@app.get("/")
def root():
    return {"status": "operational", "message": "Cult detection online."}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/analyze")
def analyze_endpoint(request: AnalysisRequest):
    # Basic input validation
    if not request.description or len(request.description.strip()) < 10:
        raise HTTPException(status_code=400, detail="Description too short.")

    if len(request.description) > 2000:
        raise HTTPException(status_code=400, detail="Description too long. Max 2000 chars.")

    # Run the chain and return the result
    try:
        result = analyze(request.description)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))