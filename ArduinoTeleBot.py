import telebot
from serial import Serial
import threading



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
            if(chesse == "1"):
                print(f"{chesse}")
                bot.send_message(self.id, "O idoso precisa de ajuda!")
                
                
                
    def __init__(self, bot):
        t = threading.Thread(target=self.voiceread)
        t.start()
        self.id = ''
        self.bot = bot

    def setid(self, id):
        self.id = id

chesse2 = threadmanager(bot=bot)

@bot.message_handler(commands=["setup", "start"])
def setup(mensagem):

    texto = "OK!"

    bot.send_message(mensagem.chat.id, texto)

    chatid = mensagem.chat.id
    #conn.write(chatid)
    chesse2.setid(chatid)

    print(chatid)

@bot.message_handler(commands=["menu"])
def menu(mensagem):
    texto = "Menu"

    bot.send_message(mensagem.chat.id, texto)

bot.polling()