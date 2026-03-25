import time
from src.llm.ollama_client import generate_response

models = ["gemma:2b", "phi3:mini", "mistral:latest"]
prompt = "Explain artificial intelligence."

for model in models:
    start = time.time()
    res = generate_response(prompt, model)
    end = time.time()

    print(f"Model: {model}")
    print(f"Latency: {end - start}\n")

