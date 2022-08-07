import telebot
import random
from telebot import types
import os

bot = telebot.TeleBot('5514650900:AAHZghYZTVBQV4D2PUEIUxXc8-KVeghQ8Jg')
          
@bot.message_handler(commands=["start"])
def start(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Открыть🃏")
        item2=types.KeyboardButton("Карты и их редкость🗂️")
        item3=types.KeyboardButton("Милкоград🍼")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(m.chat.id, 'Привет! Что бы начать открытие, нажимай на кнопки снизу👋',  reply_markup=markup)
        bot.send_sticker(m.chat.id, "CAACAgIAAxkBAAEFekFi7eXkYOFVDJOhFEKVIhVM8RVbTQACAQEAAladvQoivp8OuMLmNCkE")
        
@bot.message_handler(content_types=['text'])
def photo(message):
  if message.text == 'Открыть🃏':
  	photo = open('CARDS/' + random.choice(os.listdir('CARDS')), 'rb')
  	bot.send_photo(message.chat.id, photo, reply_to_message_id=message.message_id)
  if message.text == 'Карты и их редкость🗂️':
  	bot.reply_to(message, '''<b>КАРТЫ И ИХ РЕДКОСТЬ:</b>\n\n@zzu_61 - обычный🔵\n@Nenabobibi - обычный🔵\n@xawar228 - обычный🔵\n@ijustwntualltoshtup - обычный🔵\n@Kilkaaa662 - обычный🔵\n@garry_boy21 - обычный🔵\n\n@lriska_Milk - редкий🟢\n@fonnre - редкий🟢\n@Expirience_Gold - редкий🟢\n@shirona_shirona - редкий🟢\n@Western_shock - редкий🟢\n@BLET_SUPE - редкий🟢\n@shirona_shir0na - редкий🟢\n@myBroyyyyy - редкий🟢\n@JoRriK7 - редкий🟢\n@Epplot - редкий🟢\n@Izolenta_Kypera - редкий🟢\n@qwin0ki_oF - редкий🟢\n@Dramoed-редкий🟢\n\n@windings - эпический🟣\n@tetris_ines - эпический🟣\n@bibizyanya - эпический🟣\n@gera_oF - эпический🟣\n@tetbanjojosnus - эпический🟣\n@MechusYt - эпический🟣\n@OKUASU_ABCHIHBA - эпический🟣\n@oko_ines - эпический🟣\n@mashaluy - эпический🟣\n@legenda_pes - эпический🟣\n@elfrvioF - эпический🟣\n\n@Crade9801 - легендарный🟡\n@Krutoibober95 - легендарный🟡\n@SkocthFactit_ines - легендарный🟡\n@blag0o - легендарный🟡\n@xsv19 - легендарный🟡\n@gegestudio - легендарный🟡\n\n<b>@agentmoloko - IMPOSSIBLE☠️🍀\n@cakaoF - IMPOSSIBLE☠️🍀</b>''', parse_mode = 'HTML')
  if message.text == 'Милкоград🍼':
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Милкоград", url='https://t.me/+Zn2mJhxQkjM2NmYy')
    markup.add(button1)
    bot.reply_to(message, "Лучший чат в Млечном Пути".format(message.from_user), reply_markup=markup)
     	
     	
bot.infinity_polling(none_stop=True)