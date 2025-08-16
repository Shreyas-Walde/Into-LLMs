from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model1 = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

llm=HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model2 = ChatHuggingFace(llm=llm)

# Text generation for notes and QnA 
text = PromptTemplate(
    template = 'Generate detailed report {topic}',
    input_variables=['topic']
)

# Notes
prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

# QnA
prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
) 

# Merging into single string.txt
prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()   # why? ->  to get structured output without metadata

# To Generate text for notes and QnA
generate = text | model1 | parser

# Parallel chain
parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})    

# Merfing <Notes> and <QnA>
merge_chain = prompt3 | model1 | parser   # sequential chain

# Final chain!!!
chain = generate | parallel_chain | merge_chain

user_input = input("Enter topic for Notes and QnA: ")
result = chain.invoke({'topic': user_input})
print(result)
print(type(result))

# chain.get_graph().print_ascii()

