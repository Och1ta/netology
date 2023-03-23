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
"""

tasks = []
today = []
tomorrow = []
other = []
run = True

while run:
    command = input("Введите команду: ")
    if command == 'help':
        print(HELP)
    elif command == 'show':
        print(tasks)
    elif command == 'add':
        quest = input("Введите день добавления задачи: ")
        if quest == 'today':
            task = input("Введите название задачи: ")
            today.append(task)
        elif quest == 'tomorrow':
            task = input("Введите название задачи: ")
            tomorrow.append(task)
        elif quest == 'other':
            task = input("Введите название задачи: ")
            other.append(task)
        else:
            print("Неизвестная команда!!")
            break
        tasks = today + tomorrow + other
    elif command == 'exit':
        print("Спасибо за использование! До свидания! ")
        break
    else:
        print("Неизвестная команда!!")
        break

