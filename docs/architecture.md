# System Architecture

## Overview
This project implements a Local LLM Engineering and Benchmarking Framework
using Ollama, FastAPI, and Python. The system allows local inference,
structured output generation, benchmarking, evaluation, and experiments.

## Architecture Diagram

User Request
    ↓
FastAPI API
    ↓
Retry Handler
    ↓
Prompt Generator
    ↓
Ollama Client
    ↓
Local LLM Model
    ↓
JSON Output
    ↓
Pydantic Validation
    ↓
Return Response

## Components

### 1. FastAPI API
Handles user requests and sends prompts to the LLM system.

### 2. Retry Handler
If the model output is invalid JSON, the system retries once.

### 3. Prompt Generator
Creates structured prompts to enforce JSON output format.

### 4. Ollama Client
Sends requests to local LLM models using Ollama API.

### 5. Local LLM Models
Models used:
- Gemma 2B
- Phi3 Mini
- Mistral 7B

### 6. Validation System
Pydantic is used to validate structured JSON outputs.

### 7. Benchmarking System
Measures:
- Latency
- Tokens per second
- Memory usage

### 8. Evaluation System
Runs models on predefined prompts and stores results.

### 9. Experiment System
Experiments include:
- Temperature experiment
- Model comparison
- Quantization experiment