import requests
from time import sleep

while True:
    g = requests.get('https://api.telegram.org/bot652844002:AAFPHFs48zVNiEoNv9Yp1rpp4l2fmBjOZ20/getUpdates')
    g = requests.get('https://api.telegram.org/bot652844002:AAFPHFs48zVNiEoNv9Yp1rpp4l2fmBjOZ20/sendMessage?chat_id=292397556&text=test')
    print(g)
    print(g.text)
    sleep(60)

