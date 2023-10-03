from contact import Contact
from phonebook import PhoneBook

print("Phone Book v2.0")

pb = PhoneBook()
# добавление контактов
tmp = Contact('Иванов', 'Иван', 'Иванович', '01')
pb.add_contact(tmp)
tmp = Contact('Петров', 'Петр', 'Петрович', '02')
pb.add_contact(tmp)
tmp = Contact('Иванов', 'Петр', 'Петрович', '03')
pb.add_contact(tmp)
# вывод на экран всей книги
print(pb)
# поиск контактов, можно по нескольким полям, пустая строка означает, что поле не участвует в поиске
tmp = Contact("", "Петр", "Петрович", "")
searched = pb.search_contacts(tmp)
# вывод на экран найденных контактов
pb.print_contacts(searched)
# удаление контакта
pb.del_contact(3)
print(pb)
# изменение контакта
tmp = Contact("Трамп", "Дональд", "", "911")
pb.change_contact(2, tmp)
print(pb)
