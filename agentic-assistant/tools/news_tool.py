from langchain.tools import Tool

def get_news(topic: str) -> str:
    return f"Simulated headline for {topic}: Major developments underway."

news_tool = Tool(
    name="get_news",
    func=get_news,
    description="Get a simulated headline for a given news topic."
)