import requests

url = "https://api.telegram.org/bot5929290782:AAFdSUL4zepj1V1bBZJ7Glw6CWcNL30uaW0/sendMessage"


headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

def send_tg(trains):
    payload = f'chat_id=-1001903510887&text={trains}'
    response = requests.request("POST", url, headers=headers, data=payload)


