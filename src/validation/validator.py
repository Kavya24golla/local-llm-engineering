import json
from src.schema.output_schema import LLMOutput

def validate_output(output_text):
    try:
        data = json.loads(output_text)
        validated = LLMOutput(**data)
        return validated
    except:
        return None