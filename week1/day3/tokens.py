import os
from pathlib import Path 
from dotenv import load_dotenv 
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Api error")

client =Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"
role="user"


prompt1="Hi"
prompt2="Explain Time Travel in detail"
prompt3="Write a 1000 Word essay on ML"

#  array of prompt

prompts=[prompt1,prompt2,prompt3]

# loop through the array of prompts and send each prompt to the model for completion
for prompt in prompts:
    message={
    "role":role,
    "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model,messages=messages, max_tokens=1000)
    usage=response.usage
    print(f"Prompt: {prompt}-->your tokens : {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} total_tokens: {usage.total_tokens} finish reason : {response.choices[0].finish_reason}")



# prompt="Do u know vit bhopal university?"
# message={
#     "role":role,
#     "content":prompt
# }

# messages=[message]
# response=client.chat.completions.create(model=model,messages=messages)

    # print(response)











