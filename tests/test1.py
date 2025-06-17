import openai
import json
from config_hidden import *

client = openai.OpenAI(
    base_url="https://api.deepinfra.com/v1/openai",
    api_key=DEEPINFRA_API_KEY,
)

messages = [
    {
        "role": "user",
        "content": "Provide a JSON list of 3 famous scientific breakthroughs in the past century, all of the countries which contributed, and in what year."
    }
]

response = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    messages=messages,
    response_format={"type":"json_object"},
    tool_choice="auto",
)

print(response)