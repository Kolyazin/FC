# при отсутствии нужных файлов и папок создаются новые с заранее заданными записями.
import consts


def default_settings():
    # если существует телефонная книга в формате txt, то заново не создаю, просто выхожу
    if consts.txtBookFile.exists():
        return
    # если txt нет, на есть csv, то тоже просто выхожу
    if consts.csvBookFile.exists():
        return
    # перед созданием файла телефонной книги проверяю есть ли директория в которой книга будет храниться,
    # если нет, то создаю
    if not consts.booksFolder.exists():
        consts.booksFolder.mkdir()
    # создаю файл телефонной книги, по умолчанию в формате txt
    with open(consts.txtBookFile, 'w', encoding='utf8') as bookFile:
        for record in consts.defaultBook:
            bookFile.write(f'{record}\n')
