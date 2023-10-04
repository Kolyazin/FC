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
cond = Contact("", "Петр", "Петрович", "")
searched = pb.search_contacts(cond)

# вывод на экран найденных контактов
pb.print_contacts(searched)

# удаление контакта
pb.del_contact(3)
print(pb)

# изменение контакта
tmp = Contact("Трамп", "Дональд", "", "911")
pb.change_contact(2, tmp)
print(pb)

# сохранение в txt файл
pb.save_txt('pb.txt')

# добавляю еще контакт в текущую книгу, чтобы после чтения из файла было видно, что именно из файла прочиталось
tmp = Contact('Иванов', 'Петр', 'Петрович', '03')
pb.add_contact(tmp)
print(pb)

# чтение из txt файла
pb.read_txt('pb.txt')
print(pb)

# сохранение в csv файл
pb.save_csv('pb.csv')

# также добавляю контакт, чтобы увидеть, что прочиталось именно из файла
tmp = Contact('Иванов', 'Петр', 'Петрович', '03')
pb.add_contact(tmp)
print(pb)

# читаю из файла
pb.read_csv('pb.csv')
print(pb)
