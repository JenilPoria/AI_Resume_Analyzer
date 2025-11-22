from typing import TypedDict, List, Annotated, Literal, Optional
from .Resume_response import Resume
from pydantic import BaseModel

# Define the state model for LangGraph
class StateResquest(BaseModel):
    resume: str
    analysis: Optional[Resume] = None   
