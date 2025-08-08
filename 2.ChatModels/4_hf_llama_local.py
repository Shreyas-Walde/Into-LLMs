from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

import os

os.environ['HF_HOME'] = 'S:/campusx_lc/hf_cache'


llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature = 0.5      
        
    )
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("types of pokemon")
print(result.content)
