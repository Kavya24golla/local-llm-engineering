from fastapi import FastAPI
from src.retry.retry_handler import generate_with_retry

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Local LLM API Running"}

@app.get("/analyze")
def analyze(text: str):
    result = generate_with_retry(text)
    return {"result": str(result)}