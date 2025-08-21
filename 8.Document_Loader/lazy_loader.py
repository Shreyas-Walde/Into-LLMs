from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

# loads all the files in memory at once!
loader = DirectoryLoader(
    path=r'C:\Users\cars7\Downloads',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)  
docs = loader.lazy_load() # loads on demand
# generator object

# print(len(docs))
for documet in docs:
    print(documet.metadata)
