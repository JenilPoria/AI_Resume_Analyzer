from backend.model.Resume_response import Resume
from backend.model.Resume_request import StateResquest  
from graphs.graph_structure import app


def get_llm_response(article: str) -> Resume:
    response = app.invoke({"resume":article})
    return response["analysis"]



# def get_llm_response(article: str) -> ArticleResponse:
#     response = Main_Graph.invoke({"input":article})
#     return ArticleResponse(**response)