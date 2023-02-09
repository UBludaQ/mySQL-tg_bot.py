import telebot
#from telebot import types

import mysql.connector
from config import host, user, password, db_name

bot = telebot.TeleBot('########')

db = mysql.connector.connect(
    host=host,
    #port=3306,
    user=user,
    password=password,
    database=db_name,

    )


@bot.message_handler(content_types=['text'])
def send_start(message):
    mycursor = db.cursor()
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Приветствую, введите цифрами интересующий Вас запрос:')
    else:
        try:
            zapros = message.text
            var = zapros
            sql = f'SELECT ttn FROM user WHERE zapros =  {var} '
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            db.commit()
            my_str = f"Ваш запрос: {myresult}"
            bot.send_message(message.chat.id, my_str, parse_mode='Markdown')
        except Exception as ex:
            print(ex)
            bot.send_message(message.chat.id, 'пишите цифрами ')


if __name__ == '__main__':
    bot.polling(none_stop=True)
