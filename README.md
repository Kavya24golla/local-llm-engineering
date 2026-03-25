
## Project Summary

This project presents a **Local LLM Benchmarking and Evaluation Framework**
built using **Ollama, FastAPI, and Python** to systematically evaluate and
compare locally hosted Large Language Models (LLMs).

The framework benchmarks multiple models based on performance metrics such as
latency, token generation speed, and response length, evaluates model outputs
using standardized prompts, and performs controlled experiments including
temperature and quantization analysis. The results are aggregated into
comparison tables, visualizations, and technical reports to support model
selection for local inference environments.

This project demonstrates a complete **LLM evaluation pipeline**, including
benchmarking, evaluation, experimentation, model comparison, reporting,
and documentation.



## Experiments Conducted

The following experiments were conducted to evaluate model performance and behavior:

1. **Benchmarking**
   - Tokens per second
   - Latency
   - Response length
   - Memory usage

2. **Model Evaluation**
   - Standardized prompt testing
   - Response length comparison
   - Latency per prompt

3. **Model Comparison**
   - Combined benchmarking and evaluation metrics
   - Trade-off analysis between speed and response quality

4. **Temperature Experiment**
   - Effect of temperature on response length, latency, and generation speed

5. **Quantization Experiment**
   - Impact of model quantization on performance and memory usage
  
## Models Evaluated

The following local language models were tested:

- **Gemma 2B**
- **Phi3 Mini**
- **Mistral 7B**

  
## Key Findings

- **Phi3 Mini** achieved the lowest latency and fastest response generation.
- **Gemma 2B** generated the longest and most detailed responses.
- **Mistral 7B** produced structured responses but had higher latency.
- Temperature significantly affected response length and generation speed.
- Smaller models are more efficient for low-resource local inference environments.
- Larger models provide more detailed responses but require more computational resources.

## Conclusion

This project demonstrates a complete **Local LLM Evaluation Framework**
that enables systematic benchmarking, evaluation, experimentation,
and comparison of locally hosted language models.

The framework can be used to analyze trade-offs between performance,
response quality, and resource usage, helping in selecting appropriate
models for local deployment and inference systems.
