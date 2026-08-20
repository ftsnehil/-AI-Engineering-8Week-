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
role="user"

#####################################################################


## structure
 
from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    issue:str
    email:str
    phone_no:int

Schema=Ticket.model_json_schema()

response_formate={

    "type":"json_object"
}

system_prompt=f"""
Extract the personal information from the ticket strictly base on this schema {Schema} and Return ONLY valid JSON. 
"""

message_system={
    
    "role":"system",
    "content":system_prompt
}
 
text="Hello my name is snehil . I have an Iphone Which is not working at all . My address is bihar . my mail is abc@gmail.com . my phone no is 11223344"
prompt=f"""
This is a customer ticket . Extract the following information from the text {text} 

"""
message={
    "role":role,
    "content":prompt
}

messages=[message_system,message]
response=client.chat.completions.create(model=model,messages=messages)


answer=response.choices[0].message.content
print(answer)


## isko (data) ko padhtea kiesea hai

import json
raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)

print(ticket.name)
print(ticket.issue)
print(ticket.email)
print(ticket.phone_no)












