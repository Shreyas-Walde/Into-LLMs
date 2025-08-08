from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model='models/embedding-001', 
                             dimensions = 300)

documents = [
    "Eevee is a unique Pokemon that can evolve into multiple different forms depending on various conditions",
    "Stone is a solid mineral material forming part of the Earth's crust, often used in construction and art",
    "Fire, known as 'ka' in Egyptian and 'hi' in Japanese, is one of the four classical elements of nature",
    "Nihongo is the Japanese language, which uses three writing systems: hiragana, katakana, and kanji",
    "Machine learning models can process natural language to understand semantic relationships between words"
]

query = "pokemon that can transform into multiple forms"

doc_embedding = embedding.embed_documents(documents)
query_embedding= embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embedding)[0]

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("Similarity score is:", score)