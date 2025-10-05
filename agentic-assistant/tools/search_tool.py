from langchain.tools import Tool
import os
from langchain_community.tools.tavily_search import TavilySearchResults

# Initialize Tavily search tool
tavily = TavilySearchResults(api_key=os.getenv("TAVILY_API_KEY"))

# Wrap it in a callable function
def vacation_search(query: str) -> str:
    result = tavily.run(query)
    return result if result else "No relevant travel info found."

search_tool = Tool(
    name="search_tool",
    func=vacation_search,
    description="Use this tool to find vacation destinations, travel tips, and planning advice based on real-time web search."
)
