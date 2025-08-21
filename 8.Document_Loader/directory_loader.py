from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

# loads all the files in memory at once!
loader = DirectoryLoader(
    path=r'C:\Users\cars7\Downloads',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)  
docs = loader.load()

# print(len(docs))
print(docs[325].page_content)
print(docs[325].metadata)
