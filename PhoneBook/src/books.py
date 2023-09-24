import consts
import csv
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
    table.field_names = ['N', 'Фамилия', 'Имя', 'Отчество', 'Телефон']
    idx = 1
    for line in pb:
        table.add_row([f'{idx}'] + line.split(',', 4))
        idx += 1
    print(table)


def add_contact(pb: []) -> None:
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    name2 = input("Введите отчество: ")
    phone = input("Введите телефон: ")
    pb.append(f'{surname},{name},{name2},{phone}')
    save_book(pb)


def search_contact(pb: []) -> None:
    cmd = input(f'Поиск по: 1 - фамилии, 2 - имени, 3 - отчеству, 4 - номеру телефона, 0 - выход\n')
    search_data = input(f'Введи что искать: ')
    searched = []
    if cmd == '0':
        return
    if cmd in ['1', '2', '3', '4']:
        idx = int(cmd) - 1
    else:
        return
    for line in pb:
        if search_data == line.split(',', 4)[idx]:
            searched.append(line)
    if len(searched) == 0:
        print('Ничего не найдено!\n')
        return
    print_book(searched)


def print_contact(contact: str) -> None:
    data = contact.split(',', 4)
    print(f'Фамилия: {data[0]}\n'
          f'Имя: {data[1]}\n'
          f'Отчество: {data[2]}\n'
          f'Телефон: {data[3]}')


def del_contact(pb: []) -> None:
    idx = int(input('Введи номер строки для удаления: '))
    if idx > len(pb):
        return
    pb.pop(idx-1)
    save_book(pb)


def change_contact(pb: []) -> None:
    idx = int(input('Введи номер строки для изменения: '))
    if idx > len(pb):
        return
    data = pb[idx-1].split(',', 4)
    tmp_str = input(f'Введи новую фамилию или нажми Enter {data[0]}: ')
    if tmp_str != '':
        data[0] = tmp_str
    tmp_str = input(f'Введи новое имя или нажми Enter {data[1]}: ')
    if tmp_str != '':
        data[1] = tmp_str
    tmp_str = input(f'Введи новое отчество или нажми Enter {data[2]}: ')
    if tmp_str != '':
        data[2] = tmp_str
    tmp_str = input(f'Введи новый номер или нажми Enter {data[3]}: ')
    if tmp_str != '':
        data[3] = tmp_str
    pb[idx-1] = ','.join(data)
    save_book(pb)


def to_csv(pb: []) -> None:
    with open(consts.csvBookFile, 'w', encoding='UTF8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Фамилия', 'Имя', 'Отчество', 'Телефон'])
        for line in pb:
            writer.writerow(line.split(',', 4))
