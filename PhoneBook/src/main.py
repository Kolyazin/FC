import defaults
import books

# проверка существования файла телефонной книги и, при отсутствии создание нового
defaults.default_settings()
pb = books.load_book()
while True:
    books.print_book(pb)
    cmd = input(f'1 - Добавить, 2 - Изменить, 3 - Удалить, 4 - Найти, 5 - Вывести, 6 - В csv, 0 - Выход\n')
    if cmd == '0':
        exit(0)
    if cmd == '1':
        books.add_contact(pb)
    if cmd == '2':
        books.change_contact(pb)
    if cmd == '3':
        books.del_contact(pb)
    if cmd == '4':
        pass
    if cmd == '5':
        books.print_book(pb)
    if cmd == '6':
        pass
