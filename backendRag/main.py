from fastapi import FastAPI
from models import AIIntakeRequest, AIIntakeResponse
from openai_service import classify_message

app = FastAPI()

@app.post("/intake", response_model=AIIntakeResponse)
def intake(request: AIIntakeRequest):
    return classify_message(request.message)
