import telebot
from telebot import types 
import time 
#El programa debe estarse corriendo para que el bot funcione.
#Es recomendable usar un servidor. (Ej. raspberry)

token = #Inserte aquí su token


miBot = telebot.TeleBot(token)

chat_id = #Inserte aquí su chat ID

#Bot que te permite mandar un mensaje a la hora que le indiques.
"""
while True:
	#Trae la hora en formato de cadena.
	hora = time.strftime("%X")
	if hora == "09:21:30":
		miBot.send_message(chat_id, "¡YA DESPIÉRTATE!")
		break

"""

#Bot que te dice cuál es la hora actual al picar el botón:
@miBot.message_handler(commands = ["hora"])

def enviarHora(message):
	mensaje = "La hora actual es: "+time.strftime("%X")
	miBot.send_message(chat_id, mensaje)

markup = types.ReplyKeyboardMarkup(row_width=2)
item1 = types.KeyboardButton('/hora')
markup.add(item1)
miBot.send_message(chat_id, "Elige una opción: ", reply_markup = markup)

miBot.polling()