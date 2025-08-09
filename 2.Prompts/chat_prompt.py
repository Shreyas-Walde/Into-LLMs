from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
# Creating Dynamic set of ChatpromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, under 5 lines, what is {topic}')
    # SystemMessage(content="You are a helpful {domain} expert"),
    # HumanMessage(content="explain in min. 5 lines {topic}")
])

prompt = chat_template.invoke({'domain':'Japanese', 'topic':'te form'})

print(prompt)
