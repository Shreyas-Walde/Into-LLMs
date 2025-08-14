from langchain_google_genai import ChatGoogleGenerativeAI 
# from langchain_core.utils.function_calling import convert_to_openai_function # conversion fix 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


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

# Detailed report
prompt1 = template1.invoke({'topic': 'Snorlaxx'})
result = model.invoke(prompt1)

# detailed report -> summary
prompt2 = template2.invoke ({'text': result.content})
result_main = model.invoke(prompt2)


print(result_main.content)