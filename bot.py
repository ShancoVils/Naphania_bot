import telebot
from dotenv import load_dotenv
import os
import openai
from . import bot_settings

load_dotenv()

TOKEN = os.getenv('TELEGTAM_BOT_KEY')


CHAT_GPT_KEY = os.getenv('CHATGPT_KEY')
engine = "text-davinci-003"



bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, ама бот')


@bot.message_handler(content_types=['text'])
def text_handler(message):
    openai.api_key = os.getenv('CHATGPT_KEY')
    completion = openai.Completion.create(model=bot_settings.ENGINE,
                                          prompt=message.text,
                                          temperature=0.5,
                                          max_tokens=3500)
    bot.send_message(message.chat.id, completion.choices[0]['text'])


class Bot:
    def start_app():
        application = bot.polling()
