from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')


# # local model 
#-------------------------------------------------
# import os        # -> Running from specific location
# os.environ['HF_HOME'] = 'S:/campusx_lc/hf_cache'
# from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# llm = HuggingFacePipeline.from_model_id(
#     model_id = 'TinyLlama/TinyLlama-1.1B-Chat-v1.0',
#     task = 'text-generation',
#     pipeline_kwargs=dict(
#         max_new_tokens=50,# Set tokens to 50
#         temperature=0.7,    
#         do_sample=True 
#     )
# )
# model = ChatHuggingFace(llm=llm)
#-------------------------------------------------
while True: 
    user_input = input('You: ')
    if user_input == 'exit':
        break
    result = model.invoke(user_input)
    print("AI: ",result.content)