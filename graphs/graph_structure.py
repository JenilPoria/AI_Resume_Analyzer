from langgraph.graph import StateGraph, START, END
from schema.schema import State
from nodes.get_llm_response import get_llm_response


# Create the LangGraph
app = StateGraph(State)

# Add nodes and edges
app.add_node(get_llm_response, "get_llm_response")
app.add_edge(START, "get_llm_response")
app.add_edge("get_llm_response", END)
app = app.compile()