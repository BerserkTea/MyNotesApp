import text
import datetime


def main_menu():
    for i, item in enumerate(text.menu):
        if i == 0:
            print(item)
        else:
            print(f'\t{i}. {item}')

    while True:
        choise = input(text.input_menu)
        if choise.isdigit() and 0 < int(choise) < len(text.menu):
            return int(choise)
        else:
            print(text.input_menu_error)


def print_message(msg: str):
    print('\n' + '='*len(msg))
    print(msg)
    print('='*len(msg) + '\n')

def show_book (book: dict[int, list[str]], msg:str):
    if book:
        print('\n' + '-'* 100)
        for i, note in book.items():
            print(f'{i:>3}. {note[0]:<20} {note[1]:<20} {note[2]:<20}')
        print('-'*100 + '\n')
    else:
        print_message(msg)

def input_note(msg: str)-> list[str]:
    note = []
    date = datetime.datetime.now()
    note.append(str(date))
    for input_text in msg:
        note.append(input(input_text))
    return note

def input_request(msg: str) -> str:
    return input(msg)



