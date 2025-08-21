from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('S:\campusx_lc\8.Document_Loader\AI Roadmap_ based on Stanford AI Graduate Certificate.pdf')

docs = loader.load()  # get document object on each page

splitter = CharacterTextSplitter(
    chunk_size = 500,  # character size
    chunk_overlap = 8,   # overlap character
    separator=''    
)

result = splitter.split_documents(docs) # splitting document object
print(result[1].page_content)