# Benchmark Analysis Report

## Objective
The objective of benchmarking is to measure the performance of local language
models running on local hardware using Ollama.

## Metrics Measured
- Tokens per second (generation speed)
- Latency (response generation time)
- Response length

## Benchmark Results

| Model | Tokens/sec | Latency (s) | Response Length |
|------|-------------|-------------|----------------|
| gemma:2b | 6.47 | 32.75 | 1399 |
| phi3:mini | 4.22 | 20.60 | 513 |
| mistral:latest | 2.62 | 28.27 | 507 |

## Analysis

### Speed (Tokens/sec)
Gemma achieved the highest tokens per second, meaning it generates tokens
faster once inference starts. Mistral had the lowest tokens per second.

### Latency
Phi3 Mini had the lowest latency, meaning it produced responses faster than
the other models. Gemma had the highest latency due to longer responses.

### Response Length
Gemma generated much longer responses compared to Phi3 and Mistral, indicating
more detailed outputs.

## Conclusion
- Phi3 Mini is the fastest model in terms of latency.
- Gemma generates longer and more detailed responses.
- Mistral is slower and generates shorter responses compared to Gemma.
- Smaller models generally perform faster on local hardware.