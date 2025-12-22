from pydantic import BaseModel, Field
from typing import Literal


class AIIntakeRequest(BaseModel):
    message: str = Field(..., description="Raw customer message text")
    source: str = Field(..., description="Message source (e.g. email, form)")


class AIIntakeResponse(BaseModel):
    objectType: Literal["Case", "Lead"]
    category: str
    priority: Literal["Low", "Medium", "High"]
    sentiment: Literal["Positive", "Neutral", "Negative"]
    summary: str
    suggestedResponse: str
