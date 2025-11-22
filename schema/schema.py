from typing import TypedDict, List, Annotated, Literal, Optional
from pydantic import BaseModel
from .resume_schema import Resume

# Define the state model for LangGraph
class State(BaseModel):
    resume: str
    analysis: Optional[Resume] = None
    # analysis: Resume
