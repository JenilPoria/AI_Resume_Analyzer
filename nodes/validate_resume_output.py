from schema.schema import Resume

def validate_resume_output(output: dict) -> Resume:
    """Validate and sanitize LLM output before using it in the UI."""
    
    def ensure_list(value):
        if isinstance(value, list):
            return [str(v) for v in value]
        if value is None:
            return []
        return [str(value)]  # convert single values to list

    validated = {
        "alignment_score": float(output.get("alignment_score", 0)),
        "suggestions": ensure_list(output.get("suggestions")),
        "weaknesses": ensure_list(output.get("weaknesses")),
        "strengths": ensure_list(output.get("strengths")),
        "matched_keywords": ensure_list(output.get("matched_keywords")),
        "missing_keywords": ensure_list(output.get("missing_keywords")),
    }

    return Resume(**validated)
