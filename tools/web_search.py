# from duckduckgo_search import DDGS

# def search_web(query: str):
#     results = DDGS().text(query, max_results=5)
#     return "\n".join([r["body"] for r in results])
# from ddgs import DDGS

# def search_web(query: str):
#     with DDGS() as ddgs:
#         results = ddgs.text(query, max_results=5)

#     return "\n".join([r["body"] for r in results])
from ddgs import DDGS

def search_web(query: str):
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=5)

    return "\n".join([r["body"] for r in results])