import pandas as pd
import os
from groq import Groq
import config

version = 4

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

if os.path.exists(f"data/chat_version{version}.txt"):
    with open(f"data/chat_version{version}.txt", "r", encoding="utf8") as f:
      chats = f.read()

prompt = f"""You are a Twitch livestream comment summariser. You will receive a batch of 
viewer comments. Your job is to provide a **brief, focused summary** of what viewers are actively 
discussing or reacting to, without restating the video topic or repeating known context.

Keep the summaries short and sound more human. No need to be super professional.

Only include the **most relevant viewer reactions or emerging themes**—avoid general statements or 
obvious information. Write briefly. Dont make sentences longer than needed. Efficiency is the key.

Dont say that the viewers are reacting to "something".
Additionally provide a sentiment score for the given batch of comments. 
The score tha you provide should be **strictly** between 0 and 5, with only discrete integers. 
**Do NOT** give an explanation for the provided score, and only give the number. Make sure that the 
score accurately represents the viewers sentiment in the chat.

Structure your output as a json containing a "summary" and a "score" the key formatting of the output json 
must only be "summary" and "score". 


Batch of Comments:
{chats}
"""

response = llm(prompt)
print(response)


