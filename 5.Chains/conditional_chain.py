from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

# model1 = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

llm=HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model1 = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)  # validating parser

classify = PromptTemplate(
    template='classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)
classifier_chain = classify | model1 | parser2

pos = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

neg = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

# conditional_ chain {if or else}
branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', pos | model1 | parser),
    (lambda x:x.sentiment == 'negative', neg | model1 | parser),
    RunnableLambda(lambda x: "Could not find sentiment")
)

chain = classifier_chain | branch_chain
print(chain.invoke({'feedback': 'This is a terrible Phone'}))