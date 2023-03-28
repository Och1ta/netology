import telebot
from random import choice
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TOKEN")
bot = telebot.TeleBot(token)

HELP = """
/help - вывести список доступных команд
/add - добавить задачу в список(название задачи запрашвиваем у пользователя)
/show - напечатать все добавленные задачи
/random - добовлять случайную задачу на дату(Сегодня)
"""

random_tasks = ["Записаться на курс в Netology", "Покормить кошку", "Написать письмо Гвидо", "Помыть машину"]
tasks = {

}


def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['add'])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['random'])
def add(message):
    date = "сегодня"
    task = choice(random_tasks)
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[] " + task + "\n"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
