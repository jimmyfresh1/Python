
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

