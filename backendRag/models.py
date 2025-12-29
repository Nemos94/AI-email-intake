from pydantic import BaseModel
from typing import Optional, Literal

class AIIntakeRequest(BaseModel):
    message: str
    source: Optional[str] = "email"

class AIIntakeResponse(BaseModel):
    objectType: Literal["Case", "Lead"]
    category: Optional[str]
    priority: Literal["Low", "Medium", "High"]
    sentiment: Literal["Positive", "Neutral", "Negative"]
    summary: str
    suggestedResponse: str