import requests
from time import sleep




a = requests.get('https://api.telegram.org/bot652844002:AAFPHFs48zVNiEoNv9Yp1rpp4l2fmBjOZ20/getUpdates')
a = a.text
g = requests.get('https://api.telegram.org/bot652844002:AAFPHFs48zVNiEoNv9Yp1rpp4l2fmBjOZ20/sendMessage?chat_id=292397556&text=' + a)

sleep(10)



g = requests.get('https://api.telegram.org/bot652844002:AAFPHFs48zVNiEoNv9Yp1rpp4l2fmBjOZ20/sendMessage?chat_id=292397556&text=test02')
sleep(20)



g = requests.get('https://api.telegram.org/bot652844002:AAFPHFs48zVNiEoNv9Yp1rpp4l2fmBjOZ20/sendMessage?chat_id=292397556&text=test03')
sleep(30)
