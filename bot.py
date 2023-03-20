import telebot
from dotenv import load_dotenv
import os
import openai

load_dotenv()

TOKEN = os.getenv('TELEGTAM_BOT_KEY')
bot = telebot.TeleBot(TOKEN)

CHAT_GPT_KEY = os.getenv('CHATGPT_KEY')
engine = "text-davinci-003"


# handlers
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id

    openai.api_key = os.getenv('CHATGPT_KEY')
    engine = "text-davinci-003"
    prompt = text
    print(prompt)

    completion = openai.Completion.create(model=engine,
                                          prompt=prompt,
                                          temperature=0.5,
                                          max_tokens=1000)
    print(completion.choices[0])
    bot.send_message(chat_id, completion.choices[0]['text'])


bot.polling()
