from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

def word_count(text):
    return len(text.split())

prompt = PromptTemplate(
    template='write a joke about{topic}',
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

# parallel_chain = RunnableParallel({
#     'joke': RunnablePassthrough(), # task1 (specifying what's the task!)
#     'word_count' : RunnableLambda(word_count)  # task2
# })

# Or directly using Lambda function without creating fuction
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(), 
    'word_count' : RunnableLambda(lambda x: len(x.split()))
})  
# storing variable in lambda in form of 'x'!

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic':'japan'})
print(result)

final_result = """{} \nword count - {}""".format(result['joke'], result['word_count'])

print(final_result)