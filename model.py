from copy import deepcopy

PATH = 'note.txt'
notes_book = {}
original_book = {}


def open_file():
    global notes_book, original_book, PATH
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data, 1):
        contact = contact.strip().split(';')
        notes_book[i] = contact
    original_book = deepcopy(notes_book)


def save_file():
    global notes_book, PATH
    data = []
    for contact in notes_book.values():
        contact = ';'.join(contact)
        data.append(contact)
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)


def add_contact(new_contact: list[str]):
    global notes_book
    c_id = max(notes_book) + 1
    notes_book[c_id] = new_contact


def find_contact(word: str) -> dict[int, list[str]]:
    global notes_book
    result = {}
    for c_id, contact in notes_book.items():
        for field in contact:
            if word.lower() in field.lower():
                result[c_id] = contact
                break
    return result


def edit_contact(c_id: int, new_contact: list[str]):
    global notes_book
    current_contact = notes_book.get(c_id)
    contact = []
    for i in range(len(new_contact)):
        if new_contact[i]:
            contact.append(new_contact[i])
        else:
            contact.append(current_contact[i])
    notes_book[c_id] = contact
    return new_contact[0]


def delete_contact(c_id: int) -> str:
    global notes_book
    return notes_book.pop(c_id)[0]
