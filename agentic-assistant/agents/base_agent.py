from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.prompts import PromptTemplate
from tools.weather_tool import weather_tool
from tools.search_tool import search_tool

load_dotenv()

# Load prompt template
with open("prompts/weather_prompt.txt") as f:
    template = f.read()

weather_prompt = PromptTemplate(
    input_variables=["task"],
    template=template
)

llm = ChatOpenAI(model="gpt-4", temperature=0)

agent = initialize_agent(
    tools=[weather_tool, search_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=3,   # 👈 limit to 3 reasoning loops
    agent_kwargs={"prompt": weather_prompt}
)
