import pandas as pd
import time
from src.llm.ollama_client import generate_response

models = ["gemma:2b", "phi3:mini", "mistral:latest"]
prompt = "Explain deep learning."

results = []

for model in models:
    start = time.time()
    res = generate_response(prompt, model)
    end = time.time()

    results.append({
        "Model": model,
        "Latency": end - start
    })

df = pd.DataFrame(results)
print(df)
df.to_csv("evaluation/evaluation_results.csv", index=False)