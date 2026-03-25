import psutil
from src.llm.ollama_client import generate_response

models = ["gemma:2b", "phi3:mini", "mistral:latest"]
prompt = "Explain machine learning."

for model in models:
    start_memory = psutil.virtual_memory().used / (1024 ** 3)
    generate_response(prompt, model)
    end_memory = psutil.virtual_memory().used / (1024 ** 3)

    print(f"Model: {model}")
    print(f"Memory Used: {end_memory - start_memory} GB\n")