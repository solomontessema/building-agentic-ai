from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_core.runnables import RunnableSequence

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

prompt = PromptTemplate(
    input_variables=["question"],
    template="""
    Answer the following by reasoning step by step:
    {question}
    Let's think step by step.
    """
)


# Chain 1: Reason
reason_chain = RunnableSequence([prompt, llm, lambda x: {"thoughts": x}])


# Chain 2: Reflect
reflect_prompt = PromptTemplate(
    input_variables=["thoughts"],
    template="""
    Review the following reasoning and refine any errors:
    {thoughts}
    """
)
reflect_chain = LLMChain(llm=llm, prompt=reflect_prompt, output_key="refined")

# Chain 3: Final Answer
answer_prompt = PromptTemplate(
    input_variables=["refined"],
    template="""
    Based on the refined reasoning, what is the final answer?
    {refined}
    """
)
answer_chain = LLMChain(llm=llm, prompt=answer_prompt, output_key="final_answer")

multi_step_chain = SequentialChain(
    chains=[reason_chain, reflect_chain, answer_chain],
    input_variables=["question"],
    output_variables=["final_answer"],
    verbose=True
)

question = "If a train leaves at 3PM and travels for 5 hours, what time does it arrive?"

response = multi_step_chain.invoke({"question": question})
print(response)
