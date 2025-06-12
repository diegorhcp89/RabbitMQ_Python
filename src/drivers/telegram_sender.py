import os
from dotenv import load_dotenv
import requests

# Carrega as variáveis do .env
load_dotenv()

def send_telegram_message(message: str) -> None:
    # Obtém os valores do .env
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        raise ValueError("Token ou Chat ID não configurados no .env")

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    requests.post(url, data=payload)
