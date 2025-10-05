from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.prompts import PromptTemplate
from tools.weather_tool import weather_tool
from tools.search_tool import search_tool
from tools.news_tool import news_tool

load_dotenv()

# Load prompt template
with open("prompts/weather_prompt.txt") as f:
    template = f.read()

weather_prompt = PromptTemplate(
    input_variables=["task"],
    template=template
)

llm = ChatOpenAI(model="gpt-4", temperature=0)

from tools.news_tool import news_tool

agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
        agent_kwargs={
        "prefix": """You are a vacation planning assistant. You only answer questions related to vacations, travel destinations, trip planning, and travel advice.
If the user asks anything unrelated to vacations, politely decline and redirect them to ask about travel.

Use the VacationSearch tool when you need to look up destinations or travel tips.""",
        "format_instructions": """Use the following format:

Question: the input question you must answer
Thought: think about whether you need to use the tool
Action: the tool name (if needed)
Action Input: the input to the tool
Observation: the result from the tool
Final Answer: your final response to the user"""
    }
)
