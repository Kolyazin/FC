import contact
from prettytable import PrettyTable
class PhoneBook:
    def __init__(self):
        self.pb = []

    def __str__(self):
        table = PrettyTable()
        table.field_names = ['N', 'Фамилия', 'Имя', 'Отчество', 'Телефон']
        idx = 1
        for line in self.pb:
            table.add_row([f'{idx}'] + line)
            idx += 1
        return table.__str__()

    def add_contact(self, cont: contact) -> None:
        self.pb.append(cont)

    def del_contact(self, num: int) -> None:
        self.pb.pop(num - 1)

    def change_contact(self, num: int, cont: contact) -> None:
        self.pb[num-1] = cont

    def search_contact(self, cont: contact) -> int:
        return self.pb.index(cont)
