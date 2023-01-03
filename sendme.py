import requests
TOKEN = "5846926918:AAFoshE8rnAH9Q_klZOoCsIuGPWAJAh8qdc"
chat_id = "1959335278"

message = "hello "
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json())