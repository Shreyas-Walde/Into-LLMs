from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.utils.function_calling import convert_to_openai_function # conversion fix 
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional,Literal
from pydantic import BaseModel, Field

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# Schema
class Review(BaseModel):

    key_themes: list[str] = Field(description="Write down all the key themes dicussed in review in list") 
    summary: list[str] = Field(description="A brief summary of review")
    sentiment: Literal["pos", "neg"] = Field(description="Return sentiment of review +,- or neutral in words")

    # Optinal must have default set to None
    pros: Optional[list[str]]= Field(default=None, description= "Write down all the pros inside list")
    cons: Optional[list[str]] = Field(default=None, description = "Write down all the cons inside list")
    name: Optional[list[str]] = Field(default=None, description= "Write the name of the reviewer")

# conversion! 
review_schema = convert_to_openai_function(Review) # coverting

structured_model = model.with_structured_output(review_schema)
# review (customer's review)
result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast-whether I'm gaming, multitasking, or editing photos. The 5000mah battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
                                 
The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera-the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.
                                 
However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware-why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.
                                 
Pros :
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Cons :
Bulky and heavy-not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors
                                 
By Jacky Kazeyama
""")
# Just some stupid text above

# THE FIX: Get dictionary by taking the first element
result_dict = result[0] # converting to dict from list
# print(type(result_dict)) 

# print(result_dict)

# First, get the nested dictionary using the 'args' key
final_data = result_dict['args']
# Now access the keys from the 'final_data' dictionary
print(final_data)
# print(final_data['summary'])
print(final_data['sentiment'])