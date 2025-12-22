from fastapi import FastAPI
from models import AIIntakeRequest, AIIntakeResponse
from openai_service import analyze_message

app = FastAPI(
    title="AI Email Intake API",
    description="AI-powered intake service for classifying customer messages",
    version="1.0.0",
)

@app.post("/intake", response_model=AIIntakeResponse)
def intake(request: AIIntakeRequest):
    """
    Receives a customer message and returns a structured AI classification.
    """
    return analyze_message(request.message)
