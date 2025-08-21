from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

prompt = PromptTemplate(
    template='Answer the following questions \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://www.amazon.com/ASUS-Desktop-i7-14700F-NVIDIA%C2%AE-G16CHR-AS766Ti/dp/B0CRLF5CL5/ref=sr_1_3?crid=2OBOYV8UW3L1C&dib=eyJ2IjoiMSJ9.3lcIoDkQr5qvg-RaDAoTSpoXXEmNe5-xWqKcPPVW2VKjvWZhs8-qNII3t4lC9_wWqiKgiuLNxS4YrYeSG0STHifNK39FvrtMCFajfatAliM7zYimzbCa3WfmDg0sioRSlUvyQfFc_tUyL4MJUuPqb0X5eG7EKYOZ0OqscbjhV_J2UiDsWtmH4jtRs1y47Nh96NTi4eJIFVSdxJolr__9nDE5t6KKPnHy-5aPPMgr3e0.JBHIJX2rEdf4cDaK6_4YzuXCgHxaRWw2HzhMS8XaRtQ&dib_tag=se&keywords=ROG%2BPC&qid=1755697629&sprefix=rog%2Bp%2Caps%2C318&sr=8-3&th=1'
loader = WebBaseLoader(url)
docs = loader.load()

# docs = loader.load()
# print(len(docs))
# print(docs[0].page_content)


chain = prompt | model | parser 

print(chain.invoke({'question':'Does this pc has 2 gpu or 1?', 'text':docs[0].page_content}))