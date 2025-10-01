from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

load_dotenv()
llm = ChatOpenAI(model="gpt-4", temperature=0)

# 1: Intent Classification
intent_prompt = PromptTemplate(
    input_variables=["query"],
    template="""
    Classify the intent of this query: {query}
    Categories: weather, news, search, database, unknown.
    Just return the category.
    """
)

intent_chain = LLMChain(llm=llm, prompt=intent_prompt, output_key="category")

# 2: Generate Follow-up Prompt
followup_prompt = PromptTemplate(
    input_variables=["category"],
    template="""
    Based on the category '{category}', write a follow-up question for clarification.
    """
)
followup_chain = LLMChain(llm=llm, prompt=followup_prompt, output_key="followup")

# Combine chains
clarifier = SequentialChain(
    chains=[intent_chain, followup_chain],
    input_variables=["query"],
    output_variables=["followup"],
    verbose=True
)

result = clarifier({"query": "Tell me about weather."})
print(result["followup"])
