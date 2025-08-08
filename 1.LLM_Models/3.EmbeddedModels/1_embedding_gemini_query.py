from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model='models/embedding-001', 
                             dimensions = 32)

result = embedding.embed_query("Eve is a Pokemon")

print(str(result))


