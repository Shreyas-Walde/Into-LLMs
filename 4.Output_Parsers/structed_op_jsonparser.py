from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema 

load_dotenv()

# Define the model (if using HF API)
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 facts about {topic} \n {format_instructions}',  # Template with required variables
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}  # Correct variable name matching template
)    # generates detailed instructions for AI

chain = template | model | parser # using chain

# prompt = template.invoke({'topic': 'Kansai'})  # Provide 'topic' variable

# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
# print(final_result)

result = chain.invoke({'topic': 'Kansai'})
print(result)