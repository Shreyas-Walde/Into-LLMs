from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Generate detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer Summary from the follwing text \n {text}',
    input_variables=['text']
) 

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
parser = StrOutputParser()   # why? ->  to get structured output without metadata

chain = prompt1 | model | parser | prompt2 | model | parser

# user_input = input("Enter a topic: ")
# result = chain.invoke({'topic': user_input})
result = chain.invoke({'topic': 'Hatsune Miku'})
print(result)

chain.get_graph().print_ascii  # detailed workflow of chains