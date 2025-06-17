import openai
import json
from config_hidden import *

#BASE_URL="https://api.deepinfra.com/v1/openai"
BASE_URL = 'https://api.deepinfra.com/v1/openai'

client = openai.OpenAI(
    base_url=BASE_URL,
    api_key=DEEPINFRA_API_KEY,
)

#post_text = "Идет исследование: Физики обнаружили возможные признаки пятой силы внутри атомов"
post_text = "В России создан генератор искусственной ЭКГ с имитацией природного ритма сердца"

messages = [
    {
        "role": "user",
        "content": f"Напиши короткий, интересный комментарий к следующему посту: {post_text}"
    }
]
print(messages)

MODEL="mistralai/Mistral-7B-Instruct-v0.1"
#MODEL = 'cognitivecomputations/dolphin-2.6-mixtral-8x7b'
#MODEL = 'openchat/openchat_3.5'

response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    response_format={"type":"json_object"},
    tool_choice="auto",
    max_tokens= 150
)

print(response)