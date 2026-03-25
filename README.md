# Project Summary

This project implements a Local LLM Benchmarking and Evaluation Framework
using Ollama and FastAPI. The system evaluates multiple language models
based on performance, response quality, and generation parameters.

## Experiments Conducted
1. Benchmarking (Latency, Tokens/sec, Response Length)
2. Model Evaluation on Multiple Prompts
3. Model Comparison
4. Temperature Experiment
5. Quantization Experiment

## Models Tested
- Gemma 2B
- Phi3 Mini
- Mistral 7B

## Key Findings
- Phi3 Mini had the lowest latency.
- Gemma generated the longest and most detailed responses.
- Mistral had higher latency but structured responses.
- Temperature affected response length and generation speed.
- Smaller models are more efficient for local inference.

## Conclusion
This project demonstrates a complete local LLM evaluation pipeline including
benchmarking, evaluation, experimentation, model comparison, and reporting.