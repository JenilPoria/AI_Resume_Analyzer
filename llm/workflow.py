from .prompts.main_prompt import prompt
from .groq_client.groq_client import ste_llm

workflow = prompt | ste_llm
