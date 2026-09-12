import os
from pathlib import Path 
from dotenv import load_dotenv 
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Api error")

client =Groq(api_key=my_api_key)
model = "openai/gpt-oss-20b"

# function which will take prompt as input
def llm_ans(prompt):
    message={
        "role":"user",
        "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model,messages=messages)
    ans=response.choices[0].message.content
    return ans


# bad_prompt="""
# this is a user complaint:
# my laptop is not working
# classify this
# """
bad_prompt="""
#role:
you aare a support assistant at a laptop company.
#task
you have to classify the issue in a category
#constraints
you have to classify the issue in one of the three categories namily billing,tecghnical,reurn
#output formate
your ans should be one word only . the one world should be of the categories given in constraints
#example
for instance if a user complain syas he want a refund then the category is return 
#fallback
if the issue is unrelated to any of the categories mention in constraints, then he ans should be other

this is a user complaint:
i am not happy with my laptop
my gf left me
classify this
"""

print(llm_ans(bad_prompt))

