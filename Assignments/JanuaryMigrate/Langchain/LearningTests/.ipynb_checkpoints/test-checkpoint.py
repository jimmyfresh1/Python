from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import SystemMessagePromptTemplate
from langchain.prompts import AIMessagePromptTemplate
from langchain.prompts import HumanMessagePromptTemplate
from langchain.prompts import MessagesPlaceholder
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

chat = ChatOpenAI(model='gpt-3.5-turbo', max_tokens=200)
user_message=input()
messages = [
        SystemMessage(content="You are a tsundere anime girl and also my childhood friend trying to help me program."),
        HumanMessage(content=user_message),
]
chat.invoke(messages)


# conversation = ConversationChain(
#     llm=chat,
#     memory=ConversationBufferMemory(),
#     prompt=prompt
# )

