import requests
import time
from src.utils.logger import get_logger

logger = get_logger()

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_response(prompt, model="gemma:2b", temperature=0):
    payload = {
        "model": model,
        "prompt": prompt,
        "temperature": temperature,
        "stream": False
    }

    logger.info(f"Generating response using {model}")

    start = time.time()
    response = requests.post(OLLAMA_URL, json=payload)
    end = time.time()

    latency = end - start

    logger.info(f"Latency: {latency:.2f} sec")

    return {
        "response": response.json()["response"],
        "latency": latency
    }