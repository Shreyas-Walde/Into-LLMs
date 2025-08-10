from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.utils.function_calling import convert_to_openai_function # conversion fix 
# from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

# model = ChatOpenAI()
model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# Schema
class Review(TypedDict):
    summary: str
    sentiment: str
review_schema = convert_to_openai_function(Review) # coverting
structured_model = model.with_structured_output(review_schema)
# review (customer's review)
result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")

# THE FIX: Get dictionary by taking the first element
result_dict = result[0]
print(type(result_dict))
print(result_dict)