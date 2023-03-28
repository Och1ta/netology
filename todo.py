from random import choice

HELP = """
help - напечатать справку о программе
add - добавить задачу в список(название задачи запрашвиваем у пользователя)
_____________________________________________________________________________
команды в add:
today - добавить задачу на сегодня
tomorrow - добавить задачу на завтра
other - добавить задачу в любой другой день
_____________________________________________________________________________
show - напечатать все добавленные задачи
exit - завершить программу
random - добовлять случайную задачу на дату(Сегодня)
"""

random_tasks = ["Записаться на курс в Netology", "Покормить кошку", "Написать письмо Гвидо", "Помыть машину"]
tasks = {

}
run = True


def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
    print("Задача", task, "добавлена на дату", date)


while run:
    command = input("Введите команду: ")
    if command == 'help':
        print(HELP)
    elif command == 'show':
        date = input("Введите дату для отображения списка задач: ")
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print("Такой даты нет")
    elif command == 'add':
        date = input("Введите день добавления задачи: ")
        task = input("Введите название задачи: ")
        add_todo(date, task)
    elif command == 'random':
        task = choice(random_tasks)
        add_todo('Сегодня', task)
    elif command == 'exit':
        print("Спасибо за использование! До свидания! ")
        break
    else:
        print("Неизвестная команда!!")
        break
