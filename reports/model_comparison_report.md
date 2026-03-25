# Model Comparison Report

## Objective
The objective of model comparison is to compare multiple local language models
based on performance and output characteristics using benchmarking and
evaluation results.

## Final Comparison Table

| Model | Tokens/sec | Benchmark Latency | Benchmark Response Length | Avg Evaluation Response Length | Avg Evaluation Latency |
|------|-------------|-------------------|----------------------------|-------------------------------|------------------------|
| gemma:2b | 6.47 | 32.75 | 1399 | 1789.8 | 38.69 |
| phi3:mini | 4.22 | 20.60 | 513 | 861.6 | 25.99 |
| mistral:latest | 2.62 | 28.27 | 507 | 1194.2 | 66.23 |

## Analysis
- Phi3 Mini has the lowest latency and fastest response time.
- Gemma generates the longest and most detailed responses.
- Mistral has higher latency and moderate response length.
- Tokens per second decreases as model size increases.
- Smaller models are better for low-resource systems.
- Larger models generate more detailed responses but are slower.

## Outcome
- Best for speed → Phi3 Mini
- Best for detailed responses → Gemma
- Best for balanced output → Mistral

## Conclusion
Based on benchmarking and evaluation results, Phi3 Mini provides the best
performance for low-resource local inference. Gemma produces more detailed
responses, while Mistral provides structured responses but with higher latency.