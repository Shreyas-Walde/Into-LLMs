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
chat_history = []
while True: 
    user_input = input('You: ')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)  # .content to avoid vectors
    print("AI: ",result.content)

print(chat_history)