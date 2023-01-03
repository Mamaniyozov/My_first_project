import requests

TOKEN = "5846926918:AAFoshE8rnAH9Q_klZOoCsIuGPWAJAh8qdc"
url = f"https://api.telegram.org/bot{TOKEN}/getMe"
print(requests.get(url).json())
