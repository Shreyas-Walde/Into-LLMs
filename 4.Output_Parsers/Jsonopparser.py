from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()
#  Prompt 
template = PromptTemplate(
    template='Give me name, age, city of fictional person living in Kansai region \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = template.format()
# result = model.invoke(prompt)
# final_res = parser.parse(result.content)

chain = template | model | parser
result = chain.invoke({})     # Must pass a value eg: dict  
print(result)
print(type(result))  # json is converted to dict in py