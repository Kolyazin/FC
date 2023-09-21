# при отсутствии нужных файлов и папок создаются новые с заранее заданными записями.
import consts
from books import save_book


def default_settings() -> None:
    # если существует телефонная книга в формате txt, то заново не создаю, просто выхожу
    if consts.txtBookFile.exists():
        return
    # если txt нет, на есть csv, то тоже просто выхожу
    # if consts.csvBookFile.exists():
    #     return
    # перед созданием файла телефонной книги проверяю есть ли директория в которой книга будет храниться,
    # если нет, то создаю
    if not consts.booksFolder.exists():
        consts.booksFolder.mkdir()
    # создаю файл телефонной книги, по умолчанию в формате txt
    save_book(consts.defaultBook)
