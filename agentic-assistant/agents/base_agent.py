from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from tools.weather_tool import weather_tool
from tools.search_tool import search_tool

load_dotenv()

llm = ChatOpenAI(model="gpt-4", temperature=0)

agent = initialize_agent(
    tools=[weather_tool, search_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
