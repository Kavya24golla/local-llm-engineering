import pandas as pd
from src.llm.ollama_client import generate_response
from src.llm.prompts import (
    explanation_prompt,
    email_prompt,
    summary_prompt,
    neural_network_prompt,
    ml_prompt
)

models = ["gemma:2b", "phi3:mini", "mistral:latest"]

prompts = [
    explanation_prompt(),
    email_prompt(),
    summary_prompt(),
    neural_network_prompt(),
    ml_prompt()
]

results = []

for model in models:
    for prompt in prompts:
        res = generate_response(prompt, model)

        results.append({
            "Model": model,
            "Prompt": prompt,
            "Response Length": len(res["response"]),
            "Latency": res["latency"]
        })

df = pd.DataFrame(results)
print(df)

df.to_csv("evaluation/evaluation_results.csv", index=False)