import requests
import json
import telebot

bot = telebot.TeleBot('1740078204:AAFDI68Sfz0D0wqfu1FeEUtPOaQsQT4Qp4k')

@bot.message_handler(commands=["start"])
def start (message):
    bot.send_message(message.chat.id, "Введите номер накладной")

@bot.message_handler(content_types=['text'])
def text(message):
   
    url = "http://attachment-registry.boxberry.ru/parcels/"
    open = url + message.text
    payloads = {}
    headers = {}

    response = requests.request("GET", open, headers=headers, data=payloads)

    
    
    try:
        box = json.loads(response.text)        
        bix = box["attachments"]
    except:
        bot.send_photo(message.chat.id, "https://us.123rf.com/450wm/lkeskinen/lkeskinen1704/lkeskinen170404032/75869630-no-information-rubber-stamp-grunge-design-with-dust-scratches-effects-can-be-easily-removed-for-a-cl.jpg?ver=6")

  

    else:

    
        bot.send_message(message.chat.id, bix["title"])
        bot.send_message(message.chat.id, bix["description"])
        try:
            photo = bix["original_images"]
            for i in range(len(photo)):

                bot.send_photo(message.chat.id, photo[i])
        except KeyError:
            bot.send_photo(message.chat.id, "https://upload.wikimedia.org/wikipedia/commons/3/3d/%D0%9D%D0%B5%D1%82_%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F.jpg")

      

    

bot.polling()

# Работает если нет картинки 
# Работает если цифры введены неправильные
# Загружает все фотки (не со всех накладных)
# Комманда старт работает


