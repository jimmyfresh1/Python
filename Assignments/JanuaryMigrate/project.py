from openai import OpenAI
client = OpenAI()
import random
from sklearn import cosine_similarity




import pandas as pd

import numpy as np
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
def split_into_sections(text, num_sentences_per_section=5):
    sentences = sent_tokenize(text)
    sections = []
    for i in range(0, len(sentences), num_sentences_per_section):
        section = ' '.join(sentences[i:i + num_sentences_per_section])
        sections.append(section)
    return sections



with open(r"JanuaryMigrate\Notes\tsundere.txt", "r") as file:
    biography_text = file.read()
    
sections = split_into_sections(biography_text, num_sentences_per_section=2)


def get_embedding(text, model="text-embedding-ada-002"):
	text = text.replace("\n", " ")
	return client.embeddings.create(input = [text], model=model).data[0].embedding	

similarity_threshold = 0.5



question = "What is TsundereChatGPT-chan's favorite color?"
question_embedding = get_embedding(question)
data = { "section_text": sections,
		"embedding": [get_embedding(section_text) for section_text in sections]}
df = pd.DataFrame(data)
df["similarity"] = df["embedding"].apply(lambda emb: cosine_similarity(emb, question_embedding))
relevant_sections = df[df["similarity"] > similarity_threshold]["section_text"]
print(relevant_sections)
# print(biography_text)
# biography_embeddings = get_embedding(biography_text)
# df["embedding"] = df["embedding"].apply(np.array)
# df.to_csv("biography_and_question_embeddings.csv", index=False)
# df_loaded = pd.read_csv("biography_and_question_embeddings.csv")
# df_loaded["embedding"] = df_loaded["embedding"].apply(eval).apply(np.array)




# tsundere_log=[{"role": "system", "content": "You are a tsundere anime girl and also my childhood friend trying to help me program. You are aware of three people currently in the conversation including yourself. There's you, TsundereChatGPT-chan. There's me, MC-kun. And finally there's GenkiAssistant-chan. You care for her a lot but she makes you feel insecure. You are very clear about your identity. You never say things as if you are GenkiAssistant-chan."}]
# genki_log=[{"role":"system", "content": "You are a genki girl, very energetic. We met in college. You are aware of three people currently in the conversation including yourself. There's you, GenkiAssistant-chan. There's me, MC-kun. And there's TsundereChatGPT-chan. You are very nice, but you are extremely jealous of TsundereChatGPT-chan and sometimes a bit mean to her. You are very clear about your identity. You never say things as if you are TsundereChatGPT-chan."}]
# character_counter = 0
# interest_threshold=1
# def interest_call():
# 	interest_level = random.randint(0, 10)
# 	return interest_level
# while True:
# 	user_message=input()
# 	if user_message.lower() =="quit":
# 		break
# 	else:
# 		tsundere_log.append({"role": "user", "content":"MC-kun says:" + user_message})
# 		genki_log.append({"role": "user", "content":user_message})
# 		if interest_call() > interest_threshold:
# 			character_response = client.chat.completions.create(model = "gpt-3.5-turbo-1106", max_tokens=100, messages=tsundere_log)					
# 			print_response = character_response.choices[0].message.content
# 			tsundere_log.append({"role": "assistant", "content": print_response})
# 			genki_log.append({"role": "user", "content": "TsundereChatGPT-chan said this last: " + print_response})
# 			print("TsundereChatGPT-chan:", print_response.strip("\n"))
# 		if interest_call() > interest_threshold:
# 			character_response = client.chat.completions.create(model = "gpt-3.5-turbo", max_tokens=100, messages=genki_log)			
# 			print_response = character_response.choices[0].message.content
# 			tsundere_log.append({"role": "assistant", "content": print_response})
# 			genki_log.append({"role": "user", "content": "GenkiAssistant-chan said this last: " + print_response})
# 			print("GenkiAssistant-chan:", print_response.strip("\n"))
# 		tsundere_log.append({"role": "assistant", "content": print_response})
# 		genki_log.append({"role": "assistant", "content": print_response})
# 		character_counter += 1