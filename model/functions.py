import note
import connector


def show(number):
    logic = True
    array = connector.read_file()
    if number == 5:
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if number == 1:
            logic = False
            print(note.Note.map_note(notes))
        if number == 6:
            logic = False
            print('ID: ' + note.Note.get_id(notes))
        if number == 5:
            logic = False
            if date in note.Note.get_date(notes):
                print(note.Note.map_note(notes))
    if logic:
        print('Нет ни одной заметки...')


def add():
    note = create_note()
    array = connector.read_file()
    for notes in array:
        if note.Note.get_id(note) == note.Note.get_id(notes):
            note.Note.set_id(note)
    array.append(note)
    connector.write_file(array, 'a')
    print('Заметка добавлена...')


def delete():
    id = input('Введите id необходимой заметки: ')
    array = connector.read_file()
    logic = True
    for notes in array:
        if id == note.Note.get_id(notes):
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
        if id == note.Note.get_id(notes):
            logic = False
            note = create_note()
            note.Note.set_title(notes, note.get_title())
            note.Note.set_body(notes, note.get_body())
            note.Note.set_date(notes)
            print('Заметка изменена...')
    if logic:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    connector.write_file(array, 'a')


def create_note():
    title = input('Введите Название заметки: ')
    body = input('Введите Описание заметки: ')
    return note.Note(title=title, body=body)
