from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.assessment import AutismAssessmentResponse
from agents.analyzer import analyze_facial_expressions
import uvicorn


app = FastAPI(title="Agent Server", description="Autism assessment analysis server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze", response_model=AutismAssessmentResponse)
async def analyze_expressions(facial_expression_data: dict):
    result = analyze_facial_expressions(facial_expression_data)
    return result

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)