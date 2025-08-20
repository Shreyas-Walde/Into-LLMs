from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch
from dotenv import load_dotenv

load_dotenv()

def word_count(text):
    return len(text.split())

report = PromptTemplate(
    template='write a detailed about {topic}',
    input_variables=['topic']
)

summarize = PromptTemplate(
    template='Summarize the following {text}',
    input_variables=['text']
)

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

parser = StrOutputParser()

# report_gen_chain = RunnableSequence(report, model, parser)
report_gen_chain = report | model | parser 


# trigger when either condition is true!
branch_chain = RunnableBranch( 
    (lambda x: len(x.split())>300, RunnableSequence(summarize, model, parser)),      # (condition, runnable)
    RunnablePassthrough() # else condition
)

final_chain = RunnableSequence(report_gen_chain,branch_chain)
print(final_chain.invoke({'topic':'Ane de Armas'}))