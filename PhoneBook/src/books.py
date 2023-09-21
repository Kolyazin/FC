import consts
from prettytable import PrettyTable


def load_book() -> []:
    pb = []
    with open(consts.txtBookFile, 'r', encoding='utf8') as pbf:
        for line in pbf:
            pb.append(line.strip())
    return pb


def save_book(pb: []) -> None:
    with open(consts.txtBookFile, 'w', encoding='utf8') as bookFile:
        for record in pb:
            bookFile.write(f'{record}\n')


def print_book(pb: []) -> None:
    table = PrettyTable()
    table.field_names = ['Фамилия', 'Имя', 'Отчество', 'Телефон']
    for line in pb:
        table.add_row(line.split(',', 4))
    print(table)


def add_contact(pb: []) -> None:
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    name2 = input("Введите отчество: ")
    phone = input("Введите телефон: ")
    pb.append(f'{surname},{name},{name2},{phone}')
    save_book(pb)
