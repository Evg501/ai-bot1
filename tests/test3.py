import requests
import json
from config_hidden import *

MODEL_NAME = "mistralai/Mixtral-8x7B-Instruct-v0.1"

headers = {
    "Authorization": f"Bearer {DEEPINFRA_API_KEY}",
    "Content-Type": "application/json"
}
post_text = "Идет исследование: Физики обнаружили возможные признаки пятой силы внутри атомов"

prompt = f"Напиши короткий, интересный комментарий к следующему посту: {post_text}"

payload = {
    "model": MODEL_NAME,
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.7,
    "max_tokens": 150
}

#response = requests.post("https://api.deepinfra.com/v1/inference",  headers=headers, data=json.dumps(payload))
response = requests.post('https://api.deepinfra.com/v1/openai/chat/completions',  headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    print(response.json()["choices"][0]["message"]["content"])
else:
    print(f"Ошибка: {response.status_code}, {response.text}")
    