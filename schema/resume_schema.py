from typing import TypedDict, List, Annotated, Literal
from pydantic import BaseModel


# Define the structured output schema
class Resume(BaseModel):
    alignment_score: Annotated[float, "Alignment score out of 10 for the resume"]
    suggestions: Annotated[List[str], "List of suggestions for improving the resume"]
    weaknesses: Annotated[List[str], "List of weaknesses identified in the resume"]
    strengths: Annotated[List[str], "List of strengths identified in the resume"]
    matched_keywords: Annotated[List[str], "List of keywords that match the job description"]
    missing_keywords: Annotated[List[str], "List of keywords missing from the resume"]
