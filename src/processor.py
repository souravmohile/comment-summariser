import pandas as pd
import os
from groq import Groq
import config
from watchfiles import awatch
import asyncio

chats = "hello these are the chats"

# Function for getting the prompt
def get_prompt(chats):
    with open(f"./prompt/prompt_v{config.prompt_version}.txt", "r") as f:
        temp = f.read()
        prompt = temp.format(chats=chats)  
    return prompt

# Function to call to the LLM
def llm(prompt):
  client = Groq(api_key=config.GROQ_API_KEY)
  completion = client.chat.completions.create(
      model="meta-llama/llama-4-scout-17b-16e-instruct",
      messages=[
        {
          "role": "user",
          "content": prompt
        }
      ],
      temperature=1,
      max_completion_tokens=1024,
      top_p=1,
      stream=False,
  )

  answer = completion.choices[0].message.content 

  return answer

async def watch_file():
    async for changes in awatch("./data"):
        # changes is a set of (change_type, filepath) tuples
        for change_type, file_path in changes:
            if file_path.endswith(".txt"):
                print(f"Detected new file: {file_path}")
                with open(file_path, "r", encoding="utf8") as k:
                    chats = k.read()

                print("Getting the prompt")
                prompt = get_prompt(chats)

                print("Generating response...")
                response = llm(prompt)
                print("LLM response:", response)
