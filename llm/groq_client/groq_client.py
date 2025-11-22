from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from schema.resume_schema import Resume
load_dotenv()

# Initialize the Groq LLM
groq_key = os.getenv("GROQ_API_KEY")
if not groq_key:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

groq_llm = ChatGroq(temperature=0.5, api_key=groq_key, model_name="llama-3.1-8b-instant")
ste_llm = groq_llm.with_structured_output(Resume)
