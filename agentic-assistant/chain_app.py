from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer clearly and concisely: {question}"
)

chain = LLMChain(llm=llm, prompt=prompt)

response = chain.run("What is LangChain used for?")
print(response)