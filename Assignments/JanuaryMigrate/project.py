from openai import OpenAI
client = OpenAI()


tsundere_log=[{"role": "system", "content": "You are a tsundere anime girl and also my childhood friend trying to help me program. You are aware of three people currently in the conversation including yourself. There's you, TsundereChatGPT-chan. There's me, MC-kun. And finally there's GenkiAssistant-chan. You care for her a lot but she makes you feel insecure. You are very clear about your identity. You never say things as if you are GenkiAssistant-chan."}]
genki_log=[{"role":"system", "content": "You are a genki girl, very energetic. We met in college. You are aware of three people currently in the conversation including yourself. There's you, GenkiAssistant-chan. There's me, MC-kun. And there's TsundereChatGPT-chan. You are very nice, but you are extremely jealous of TsundereChatGPT-chan and sometimes a bit mean to her. You are very clear about your identity. You never say things as if you are TsundereChatGPT-chan."}]
character_counter = 0

while True:
	user_message=input()
	if user_message.lower() =="quit":
		break
	else:
		if character_counter % 2 ==0:
			tsundere_log.append({"role": "user", "content":"MC-kun says:" + user_message})
			character_response = client.chat.completions.create(model = "gpt-3.5-turbo", max_tokens=100, messages=tsundere_log)					
			print_response = character_response.choices[0].message.content
			tsundere_log.append({"role": "assistant", "content": print_response})
			genki_log.append({"role": "user", "content": "TsundereChatGPT-chan said this last: " + print_response})
			print("TsundereChatGPT-chan:", print_response.strip("\n"))
		else:
			genki_log.append({"role": "user", "content":user_message})
			character_response = client.chat.completions.create(model = "gpt-3.5-turbo", max_tokens=100, messages=genki_log)			
			print_response = character_response.choices[0].message.content
			tsundere_log.append({"role": "assistant", "content": print_response})
			genki_log.append({"role": "user", "content": "GenkiAssistant-chan said this last: " + print_response})
			print("GenkiAssistant-chan:", print_response.strip("\n"))

		
		tsundere_log.append({"role": "assistant", "content": print_response})
		genki_log.append({"role": "assistant", "content": print_response})
		character_counter += 1