from langchain.tools import Tool

def get_weather(city: str) -> str:
    return f"Simulated weather for {city}: Sunny, 24°C."

weather_tool = Tool(
    name="get_weather",
    func=get_weather,
    description="Fetch simulated weather data for a given city."
)