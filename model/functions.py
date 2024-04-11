import model.note
import model.connector as connector


def show(number):
    logic = True
    array = connector.read_file()
    if number == 5:
        date = input('Введите дату в формате dd.mm.yyyy: ')
    if number == 6:
        id = input('Введите id необходимой заметки: ')
    for notes in array:
        if number == 1:
            logic = False
            print(model.note.Note.map_note(notes))
        if number == 6:
            logic = False
            if id == model.note.Note.get_id(notes):
                print(model.note.Note.map_note(notes))
            # print('ID: ' + model.note.Note.get_id(notes))
        if number == 5:
            logic = False
            if date in model.note.Note.get_date(notes):
                print(model.note.Note.map_note(notes))
    if logic:
        print('Нет ни одной заметки...')


def add():
    note = create_note()
    array = connector.read_file()
    for notes in array:
        if model.note.Note.get_id(note) == model.note.Note.get_id(notes):
            model.note.Note.set_id(note)
    array.append(note)
    connector.write_file(array, 'a')
    print('Заметка добавлена...')


def delete():
    id = input('Введите id необходимой заметки: ')
    array = connector.read_file()
    logic = True
    for notes in array:
        if id == model.note.Note.get_id(notes):
            logic = False
            array.remove(notes)
            print('Заметка удалена...')
    if logic:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    connector.write_file(array, 'a')


def edit():
    id = input('Введите id необходимой заметки: ')
    array = connector.read_file()
    logic = True
    for notes in array:
        if id == model.note.Note.get_id(notes):
            logic = False
            note = create_note()
            model.note.Note.set_title(notes, note.get_title())
            model.note.Note.set_body(notes, note.get_body())
            model.note.Note.set_date(notes)
            print('Заметка изменена...')
    if logic:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    connector.write_file(array, 'a')


def create_note():
    title = input('Введите Название заметки: ')
    body = input('Введите Описание заметки: ')
    return model.note.Note(title=title, body=body)
