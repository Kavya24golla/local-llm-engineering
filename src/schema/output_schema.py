from pydantic import BaseModel

class LLMOutput(BaseModel):
    summary: str
    sentiment: str
    confidence: float