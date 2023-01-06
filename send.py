import requests
import json
token = "5846926918:AAFoshE8rnAH9Q_klZOoCsIuGPWAJAh8qdc"

chat_id1=1959335278
TOKEN = '5846926918:AAFoshE8rnAH9Q_klZOoCsIuGPWAJAh8qdc'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

response = requests.get(url=BASE_URL)
updates=response.json()['result']
num_updates = len(updates["result"])
last_update = num_updates - 1
text = updates["result"][last_update]["message"]["text"]
chat_id = updates["result"][last_update]["message"]["chat"]["id"]
while True:
    updates=last_update
    if chat_id!=updates["result"][num_updates]["message"]["chat"]["id"]:
        message=text
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        response=requests.get(url).json()
        print(response)