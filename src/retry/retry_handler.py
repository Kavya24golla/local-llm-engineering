from src.llm.ollama_client import generate_response
from src.validation.validator import validate_output

def generate_with_retry(text, model="gemma:2b"):
    prompt = f"""
    Analyze the following text and respond ONLY in JSON:

    {{
        "summary": "...",
        "sentiment": "...",
        "confidence": 0.0
    }}

    Text: {text}
    """

    result = generate_response(prompt, model)
    validated = validate_output(result["response"])

    if validated:
        return validated

    print("Retrying...")
    result = generate_response(prompt, model)
    validated = validate_output(result["response"])

    if validated:
        return validated

    return "Failed after retry"