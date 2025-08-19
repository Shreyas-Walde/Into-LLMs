from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()


Tweet = PromptTemplate(
    template='Generate a tweet about{topic}',
    input_variables=['topic']
)
LinkedIn = PromptTemplate(
    template='Generate a LinkedIn post about{topic}',
    input_variables=['topic']
)

model1 = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
model2 = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
parser = StrOutputParser()


parallel_chain = RunnableParallel({
    'tweet' : RunnableSequence(Tweet,model1,parser),
    'linkedin' : RunnableSequence(LinkedIn, model2, parser)
})

print(parallel_chain.invoke({'topic':'AI'}))
print(parallel_chain.invoke({'topic':'AI'})['tweet'])