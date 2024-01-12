from gpt4all import GPT4All
model = GPT4All("gpt4all-falcon-newbpe-q4_0.gguf")

joke = "Why did the chicken cross the road? To get to the other side."
system_template = "A man tells a top-notch judge a joke; the judge gives his judgment of the joke."

prompt_template = 'Man: {0}\njudge: '

with model.chat_session(system_template, prompt_template):
    print('Judge:', model.generate(joke))
#     print ('-------')

# with model.chat_session():
#     response1 = model.generate(prompt='hello', temp=0)
#     response2 = model.generate(prompt='write me a short poem', temp=0)
#     response3 = model.generate(prompt='thank you', temp=0)
#     print(model.current_chat_session)