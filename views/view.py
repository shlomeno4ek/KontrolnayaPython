import controllers.controller as ctrl


def menu():
    print("\nИмеются следующие команды:\n\n"
          "all - вывод всех заметок из файла\n"
          "add - добавление заметки\n"
          "delete - удаление заметки\n"
          "edit - редактирование заметки\n"
          "date - выборка заметок по дате\n"
          "id - показать заметку по id\n"
          "exit - выход\n\n"
          "Введите команду: ")


def start():
    print("Это программа 'Заметки'.")
    flag = True
    while flag:
        menu()
        command = input()
        if ctrl.is_exit(command):
            print("До свидания!")
            flag = False
        elif ctrl.is_valid_command(command):
            ctrl.change_commands(command)
        else:
            print("Ошибка! Такой команд нет в списке!")
