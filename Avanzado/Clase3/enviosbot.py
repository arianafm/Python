import telebot

token = #Inserte aquí su token

miBot = telebot.TeleBot(token)

@miBot.message_handler(commands = ['start','help'])

def send_welcome(message):
	miBot.reply_to(message, "Hola, soy tu bot de Python :) ")


chat_id = #Inserte aquí su chat ID

miBot.send_message(chat_id, "H O L A")
#Aquí lo estamos abriendo en bits.
file = open("pug.png", "rb") #rb : read in bits
miBot.send_photo(chat_id,file)

doc = open("miprimerbot.py","rb")
miBot.send_document(chat_id,doc)

latitud = 19.324392
longitud = -99.179703
miBot.send_location(chat_id,latitud,longitud)

miBot.polling()