from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)


# Step 1: Analyze Query Intent
intent_prompt = PromptTemplate(
    input_variables=["user_query"],
    template="Determine the intent of this query: {user_query}"
)
intent_chain = LLMChain(llm=llm, prompt=intent_prompt, output_key="intent")

# Step 2: Recommend Tool or Action
recommend_prompt = PromptTemplate(
    input_variables=["intent"],
    template="Based on intent '{intent}', recommend a suitable tool or next step."
)
recommend_chain = LLMChain(llm=llm, prompt=recommend_prompt, output_key="recommendation")

# Compose chain
full_chain = SequentialChain(
    chains=[intent_chain, recommend_chain],
    input_variables=["user_query"],
    output_variables=["recommendation"],
    verbose=True
)

result = full_chain({"user_query": "What’s the stock price of Tesla today?"})
print(result["recommendation"])