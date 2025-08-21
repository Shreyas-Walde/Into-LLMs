from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('AI Roadmap_ based on Stanford AI Graduate Certificate.pdf')  # best with text data

docs = loader.load()

print(docs)
print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)