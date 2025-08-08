from langchain_huggingface import HuggingFaceEmbeddings

import os
os.environ['HF_HOME'] = 'S:/campusx_lc/hf_cache'

embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Eve is pokemon",
    "Stone is a rock",
    "fire is ka or hi",
    "nihongo is japanese"
]
result = embedding.embed_documents(documents)
print(str(result))

# result = embedding.embed_query("Eve is a Pokemon")
# print(str(result))
