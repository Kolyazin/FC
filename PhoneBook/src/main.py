import defaults
import books

# проверка существования файла телефонной книги и, при отсутствии создание нового
defaults.default_settings()
pb = books.load_book()
books.print_book(pb)
books.add_contact(pb)
books.save_book(pb)
