from langchain.tools import Tool

def web_search(query: str) -> str:
    return f"Simulated search result for: {query}"

search_tool = Tool(
    name="web_search",
    func=web_search,
    description="Simulate a web search for a given query."
)