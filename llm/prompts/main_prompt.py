from langchain.prompts import ChatPromptTemplate




# Define the system prompt for the LLM
system_prompt = """You are an expert Resume Evaluation Assistant that helps candidates refine and optimize their resumes to align with a specific job role.
You must:
- Provide an alignment score out of 10 for the resume.
- List suggestions for improvement.
- List weaknesses in the resume.
- List strengths in the resume.
- List matched keywords.
- List missing keywords.

You MUST return your analysis in the structured function-call format provided.
Do NOT output JSON manually.
The model will format the result automatically.
"""


# Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "Here is the resume: {resume}")
])