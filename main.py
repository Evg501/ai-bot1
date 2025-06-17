import requests
import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from config_hidden import *

# === Настройки ===
#TELEGRAM_TOKEN = 'ВАШ_TELEGRAM_ТОКЕН'
#DEEPINFRA_API_KEY = 'ВАШ_DEEPINFRA_КЛЮЧ'

MODEL_NAME = "mistralai/Mixtral-8x7B-Instruct-v0.1"
#MODEL_NAME = "cognitivecomputations/dolphin-2.6-mixtral-8x7b"

# === Генерация комментария через DeepInfra ===
def generate_comment(post_text):
    headers = {
        "Authorization": f"Bearer {DEEPINFRA_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"Напиши короткий, интересный комментарий на русском языке к следующему посту: {post_text}"

    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 150
    }

    #response = requests.post("https://api.deepinfra.com/v1/inference",  headers=headers, data=json.dumps(payload))
    response = requests.post('https://api.deepinfra.com/v1/openai/chat/completions',  headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Ошибка: {response.status_code}, {response.text}"

# === Команда /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я готов комментировать новые посты!")

# === Обработка новых сообщений ===
async def handle_new_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    # Проверяем, что это текстовый пост
    if message.text and len(message.text) > 10:
        post_text = message.text
        await update.message.reply_text("Пишу комментарий...")
        comment = generate_comment(post_text)
        await update.message.reply_text(f"Комментарий от ИИ:\n{comment}")
    elif len(message.text)<=10:
        await update.message.reply_text("Короткое сообщение...")
    
# === Запуск бота ===
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_new_post))

print("Бот запущен и ждёт новые посты...")
app.run_polling()