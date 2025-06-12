import requests

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    requests.post(url, data=payload)

token = "7378913312:AAHNvn7VBizIddVYFxgtvhmKXOgqBpxEp_Q"
chat_id= -1002658882522
message = "Estou no telegram em Python!!!"

send_telegram_message(token, chat_id, message)
