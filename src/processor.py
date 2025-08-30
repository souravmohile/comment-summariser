import pandas as pd
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
comments = ""
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
def llm(prompt):
  client = Groq()
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

description = """LIVE COVERAGE: Johnny Depp v Amber Heard Defamation Trial

Happening in court:
Plaintiff Opening Statement - Benjamin Chew
Plaintiff Opening Statement - Camille Vasquez
Break
Respondent Opening Statement-J Benjamin Rottenborn-Amber Heard’s Attorney
Opening Statement - Elaine Bredehoft - Amber Heard’s Attorney
LUNCH BREAK 
Christi Dembrowski - Johnny Depp's Sister

Actor Johnny Depp is suing ex-wife Amber Heard for $50 million  for defamation in connection with Heard’s 2018 Washington Post op-ed, in which she spoke out about being the victim of domestic violence. Heard’s article did not specifically name Depp as her alleged abuser, but according to Depp’s lawsuit, it relied “on the central premise that Ms. Heard was a domestic abuse victim and that Mr. Depp perpetrated domestic violence against her.” Amber Heard is counter-suing Depp for $100 million. 

The defamation trial began Monday in Fairfax County Circuit Court in Virginia, with jury selection completing on the same day. There is a possibility of celebrity witnesses testifying, including James Franco and Elon Musk. Tune in to the Law&Crime Network for daily coverage of this high-profile trial. 

#JohnnyDepp #AmberHeard
"""
prompt = f"""You are a YouTube livestream comment summariser. You will receive a batch of viewer comments. Your job is to provide a **brief, focused summary** of what viewers are actively discussing or reacting to, without restating the video topic or repeating known context.
Only include the **most relevant viewer reactions or emerging themes**—avoid general statements or obvious information already found in the video description.

Video Description:
{description}

Comments:
{comments}
"""
response = llm(prompt)
print(response)

# def stream():
#     for i in comments:
#         print(i)
#         time.sleep(np.random.uniform(0, 2))
# stream()

# temp1 = []
# start_time = time.time()
# while time.time() - start_time < 3:
#     for i in comments:
#         temp1.append(i)
#         time.sleep(np.random.uniform(0, 2))

# print(temp1)
