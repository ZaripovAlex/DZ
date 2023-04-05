def inputTitle():
    try:
        return input("Введите заголовок: ")
    except Exception as e:
        print(f"Ошибка {e}")


def inputnote():
    try:
        return input("Введите текст заметки: ")
    except Exception as e:
        print(f"Ошибка {e}")

def inputnoteID():
    try:
        return int(input("Введите номер заметки: "))
    except Exception as e:
        print(f"Ошибка {e}")

def printMenu():
    print("Выберите - что хотите сделать: "
          "\n1 - Создать заметку "
          "\n2 - Изменить заметку "
          "\n3 - Вывести все заметки "
          "\n4 - Удаление заметку "
          )

def printSeparator():
    print('---------------------')

def print_data(note):
    for d in note:
        print(f"ID: {d[0]}")
        print(f"Заголовок: {d[1]}")
        print(f"Заметка: {d[2]}")
        printSeparator()

def print_data1(note, noteId):
    print(f"ID: {noteId}")
    print(f"Заголовок: {note[0]}")
    print(f"Заметка: {note[1]}")
    printSeparator()

def inputСhoose(message: str = f'Ваш выбор (Что бы повторить меню - 5) > ') -> int:
    try:
        return int(input(message))
    except Exception as e:
        print(f"Ошибка {e}")