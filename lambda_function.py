import json
import os
import requests

def lambda_handler(event, context):
    telegram_msg = event #json.dumps(event)
    telegram_msg = telegram_msg['message']['text']
    #telegram_msg = 'plain text'
    
    chat_id = os.environ['CHAT_ID']
    telegram_token = os.environ['TELEGRAM_TOKEN']
    
    api_url = f"https://api.telegram.org/bot{telegram_token}/"

    params = {'chat_id': chat_id, 'text': telegram_msg}
    res = requests.post(f"{api_url}sendMessage", data=params).json()
    
