from schema.schema import State
from llm.workflow import workflow
from llm.groq_client.groq_client import ste_llm
# Define the function to get the LLM response
def get_llm_response(state: State) -> State:
    response = workflow.invoke({"resume": state.resume})
    state.analysis = response
    return state



# def reevaluate_keywords(state : SummaryState) -> SummaryState:
#     summary = state.summary[-1]
#     keywords = state.keyword[-1]
#     article = state.input
#     response = llm.invoke(evaluate_prompt.format_messages(input = article,summary=summary, keywords=', '.join(keywords))).content
#     score = float(response)
#     state.confidence_score.append(score)
#     return state
