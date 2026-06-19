# %%
# pip install pytelegrambotapi

# %%
import telebot

CHAVE_API = "TELEGRAM_BOT_TOKEN_AQUI"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["reserva"])
def responder(mensagem):
  bot.reply_to(mensagem, "Para qual data deseja fazer uma reserva?")

@bot.message_handler(commands=["consulta"])
def responder(mensagem):
  pass

@bot.message_handler(commands=["cancelar"])
def responder(mensagem):
  pass


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
    /reserva - Para fazer uma reserva
    /consulta - Para conferir sua a sua reserva
    /cancelar - Para cancelar a sua reserva
Responder qualquer outra coisa não vai funcionar, clique em uma das opções."""
    bot.reply_to(mensagem, texto)

bot.polling()
