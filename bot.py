import requests
from time import sleep
import os

g = requests.get('https://api.telegram.org/bot652844002:AAFPHFs48zVNiEoNv9Yp1rpp4l2fmBjOZ20/getUpdates')
g = requests.get('https://api.telegram.org/bot652844002:AAFPHFs48zVNiEoNv9Yp1rpp4l2fmBjOZ20/sendMessage?chat_id=292397556&text=test')
print(g)
print(g.text)
sleep(60)


TOKEN = "652844002:AAFPHFs48zVNiEoNv9Yp1rpp4l2fmBjOZ20"
PORT = int(os.environ.get('PORT', '8443'))
updater = updater(TOKEN)
# add handlers
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://telega-bot-eastol.herokuapp.com/" + TOKEN)
updater.idle()




g = requests.get('https://api.telegram.org/bot652844002:AAFPHFs48zVNiEoNv9Yp1rpp4l2fmBjOZ20/getUpdates')
g = requests.get('https://api.telegram.org/bot652844002:AAFPHFs48zVNiEoNv9Yp1rpp4l2fmBjOZ20/sendMessage?chat_id=292397556&text=test')
print(g)
print(g.text)
sleep(60)


TOKEN = "652844002:AAFPHFs48zVNiEoNv9Yp1rpp4l2fmBjOZ20"
PORT = int(os.environ.get('PORT', '8443'))
updater = updater(TOKEN)
# add handlers
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://telega-bot-eastol.herokuapp.com/" + TOKEN)
updater.idle()


g = requests.get('https://api.telegram.org/bot652844002:AAFPHFs48zVNiEoNv9Yp1rpp4l2fmBjOZ20/getUpdates')
g = requests.get('https://api.telegram.org/bot652844002:AAFPHFs48zVNiEoNv9Yp1rpp4l2fmBjOZ20/sendMessage?chat_id=292397556&text=test')
print(g)
print(g.text)
sleep(60)
