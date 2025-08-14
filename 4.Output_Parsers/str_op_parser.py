from langchain_google_genai import ChatGoogleGenerativeAI 
# from langchain_core.utils.function_calling import convert_to_openai_function # conversion fix 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# 1st Prompt -> Detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd Prompt -> Summary
template2 = PromptTemplate(
    template='Write a five line summary of text. \n {text}',
    input_variables=['text']
)


# paser
parser = StrOutputParser()

# chaining
chain = template1 | model | parser | template2 | model | parser 

result = chain.invoke({'topic': 'Eve Pokemon'})
print(result)