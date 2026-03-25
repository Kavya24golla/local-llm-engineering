def explanation_prompt():
    return "Explain artificial intelligence in simple words."

def email_prompt():
    return "Write a professional email requesting internship."

def summary_prompt():
    return "Summarize climate change in simple terms."

def neural_network_prompt():
    return "Explain neural networks in simple terms."

def ml_prompt():
    return "What is machine learning?"

def json_analysis_prompt(text):
    return f"""
Respond ONLY in JSON format:
{{
    "summary": "...",
    "sentiment": "...",
    "confidence": 0.0
}}

Text: {text}
"""