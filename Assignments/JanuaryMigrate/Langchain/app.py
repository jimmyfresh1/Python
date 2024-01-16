import os
from openai import AsyncOpenAI


from chainlit.playground.providers.openai import ChatOpenAI
import chainlit as cl


client = AsyncOpenAI()

import os
from openai import AsyncOpenAI


from chainlit.playground.providers.openai import ChatOpenAI
import chainlit as cl


client = AsyncOpenAI(api_key="YOUR_OPENAI_API_KEY")

@cl.step(type="llm", root=True, language="sql")
async def text_to_sql(text: str):
    # Create a ChatGeneration to enable the prompt playground
    generation = cl.ChatGeneration(
        provider=ChatOpenAI.id,
        messages=[
            cl.GenerationMessage(
                role="user",
                template=template,
                formatted=template.format(input=text),
            )
        ],
        settings=settings,
        inputs={"input": text},
    )

    # Call OpenAI
    stream = await client.chat.completions.create(
        messages=[m.to_openai() for m in generation.messages], stream=True, **settings
    )

    current_step = cl.context.current_step

    async for part in stream:
        if token := part.choices[0].delta.content or "":
            await current_step.stream_token(token)

    generation.completion = current_step.output

    current_step.generation = generation


@cl.on_message
async def main(message: cl.Message):
    await text_to_sql(message.content)

