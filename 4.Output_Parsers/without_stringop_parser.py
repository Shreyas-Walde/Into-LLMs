from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate

import os
os.environ['HF_HOME'] = 'S:/campusx_lc/hf_cache'


llm = HuggingFacePipeline.from_model_id(
    model_id = 'TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task = 'text-generation',
    pipeline_kwargs=dict(
        temperature = 1.6,
        max_new_tokens=200
        
    )
)

model = ChatHuggingFace(llm=llm)

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
prompt1 = template1.invoke({'topic': 'Snorlax'})
result = model.invoke(prompt1)

# detailed report -> summary
prompt2 = template2.invoke ({'text': result.content})
result_main = model.invoke(prompt2)


print(result_main.content)