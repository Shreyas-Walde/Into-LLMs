from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()


prompt1 = PromptTemplate(
    template='write a joke about{topic}',
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

joke_chain = RunnableSequence(prompt1, model, parser)
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explaination': RunnableSequence(prompt2, model, parser)
})

chain = RunnableSequence(joke_chain, parallel_chain)

print(chain.invoke({'topic':'Hans Zimmers music'}))