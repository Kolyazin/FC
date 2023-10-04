from contact import Contact
import csv
from prettytable import PrettyTable


class PhoneBook:
    def __init__(self):
        self.pb = []

    # красиво вывожу используя библиотеку PrettyTable
    def __str__(self):
        table = PrettyTable()
        table.field_names = ['N', 'Фамилия', 'Имя', 'Отчество', 'Телефон']
        idx = 1
        for line in self.pb:
            table.add_row([f'{idx}'] + line)
            idx += 1
        return table.__str__()

    def add_contact(self, cont: Contact) -> None:
        self.pb.append(cont)

    def del_contact(self, num: int) -> None:
        self.pb.pop(num - 1)

    def change_contact(self, num: int, cont: Contact) -> None:
        self.pb[num - 1] = cont

    # поиск контактов возвращает список порядковых номеров контактов
    def search_contacts(self, cont: Contact) -> []:
        idx = 1
        result = []
        for item in self.pb:
            if cont == item: # сравнение с использованием переопределенного __eq__ в классе contact
                result.append(idx)
            idx += 1
        return result

    def print_contacts(self, ids: []) -> None:
        table = PrettyTable()
        table.field_names = ['N', 'Фамилия', 'Имя', 'Отчество', 'Телефон']
        for idx in ids:
            table.add_row([f'{idx}'] + self.pb[idx - 1])
        print(table)

    def save_txt(self, file_name):
        with open(file_name, 'w', encoding='utf8') as fn:
            for cont in self.pb:
                fn.write(f'{",".join(cont.get())}\n')

    def read_txt(self, file_name):
        with open(file_name, 'r', encoding='utf8') as fn:
            tmp_pb = []
            for line in fn:
                tmp_pb.append(Contact(*line.strip().split(',', 4)))
            self.pb = tmp_pb

    def save_csv(self, file_name):
        with open(file_name, 'w', encoding='utf8') as fn:
            writer = csv.writer(fn)
            # writer.writerow(['Фамилия', 'Имя', 'Отчество', 'Телефон'])
            for cont in self.pb:
                writer.writerow(cont.get())

    def read_csv(self, file_name):
        with open(file_name, 'r', encoding='utf8') as fn:
            reader = csv.reader(fn)
            tmp_pb = []
            for line in reader:
                tmp_pb.append(Contact(*line))
            self.pb = tmp_pb
