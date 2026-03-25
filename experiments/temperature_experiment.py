import pandas as pd
import time
from src.llm.ollama_client import generate_response
from src.llm.prompts import email_prompt
from src.utils.logger import get_logger

logger = get_logger()

prompt = email_prompt()
temps = [0, 0.2, 0.5, 0.7, 1.0]

results = []

for t in temps:
    logger.info(f"Running temperature {t}")

    start = time.time()
    res = generate_response(prompt, model="gemma:2b", temperature=t)
    end = time.time()

    latency = end - start
    tokens = len(res["response"].split())
    tokens_per_sec = tokens / latency

    results.append({
        "Temperature": t,
        "Tokens/sec": round(tokens_per_sec, 2),
        "Latency (s)": round(latency, 2),
        "Response Length": len(res["response"])
    })

df = pd.DataFrame(results)
print(df)

df.to_csv("experiments/results/temperature_results.csv", index=False)

logger.info("Temperature experiment completed")