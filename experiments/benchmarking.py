import time
import pandas as pd
from src.llm.ollama_client import generate_response
from src.llm.prompts import explanation_prompt
from src.utils.logger import get_logger

logger = get_logger()

models = ["gemma:2b", "phi3:mini", "mistral:latest"]
prompt = explanation_prompt()

results = []

for model in models:
    logger.info(f"Benchmarking {model}")

    start = time.time()
    res = generate_response(prompt, model)
    end = time.time()

    latency = end - start
    tokens = len(res["response"].split())
    tokens_per_sec = tokens / latency

    results.append({
        "Model": model,
        "Tokens/sec": round(tokens_per_sec, 2),
        "Latency (s)": round(latency, 2),
        "Response Length": len(res["response"])
    })

df = pd.DataFrame(results)
print(df)

df.to_csv("benchmarking/benchmark_results.csv", index=False)

logger.info("Benchmark completed")