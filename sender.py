import os
from dotenv import load_dotenv
import requests

load_dotenv()  # Carrega as variáveis do arquivo .env

def send_telegram_message(message):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    requests.post(url, data=payload)

message = "Estou no telegram em Python!!!"
send_telegram_message(message)
