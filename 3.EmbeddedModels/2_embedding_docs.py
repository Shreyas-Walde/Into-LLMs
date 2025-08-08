from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model='models/embedding-001', 
                             dimensions = 32)

documents = [
    "Eve is pokemon",
    "Stone is a rock",
    "fire is ka or hi",
    "nihongo is japanese"
]
result = embedding.embed_documents(documents)

print(str(result))


