import telebot
from serial import Serial
import threading
import time



serial_port = 'COM4'
boud_rate = 115200

conn = Serial(serial_port, boud_rate)

key = "5479250646:AAF4Gqb8iyopPIZU-Eb2auHWJkmFAXx5Uc8"
bot = telebot.TeleBot(key)


class threadmanager:
    def voiceread(self):
        while(1):
            chesse = conn.readline()
            numeric_filter = filter(str.isdigit, str(chesse))
            chesse = "".join(numeric_filter)
            print(f"{chesse}")
            self.chesse1 = chesse
            print(f"a{self.chesse1}")

            if(self.chesse1 == "1"):
                bot.send_message(self.id, "velhinho")
                
                
                
    def __init__(self, bot):
        t = threading.Thread(target=self.voiceread)
        t.start()
        self.id = ''
        self.bot = bot

    def setid(self, id):
        self.id = id

chesse2 = threadmanager(bot=bot)

@bot.message_handler(commands=["setup"])
def setup(mensagem):

    texto = "OK!"

    bot.send_message(mensagem.chat.id, texto)

    chatid = mensagem.chat.id
    chesse2.setid(chatid)

    print(chatid)

@bot.message_handler(commands=["velho"])
def socorro(mensagem):

    texto = "seu velho esta morrendo"

    print(chesse2.chesse1)

    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["menu"])
def menu(mensagem):
    texto = "ê macarena"

    bot.send_message(mensagem.chat.id, texto)

bot.polling()