import requests
TOKEN = '5846926918:AAFoshE8rnAH9Q_klZOoCsIuGPWAJAh8qdc'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

response = requests.get(url=BASE_URL)
updates=response.json()['result']
 
for update in updates:
    msg = update['message']
    
    print(msg)

