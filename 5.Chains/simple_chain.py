from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Define the model (if using HF API)
# llm = HuggingFaceEndpoint(
#     repo_id="google/gemma-2-2b-it",
#     task="text-generation"
# )

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

prompt = PromptTemplate(
    template = 'Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser
user_topic = input("Enter a topic: ")
result = chain.invoke({'topic':user_topic})

print(result)
# chain.get_graph().print_ascii()   # to get graphs 

print(type(result))