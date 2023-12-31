class Contact:
    # переопределил оператор равенства при сравнении
    # пустые поля у переменной в левой части означают, что при любом значении в правой части результат будет True
    def __eq__(self, other):
        result = True
        result = True if (result is True and (self.surname == other.surname or self.surname == "")) else False
        result = True if (result is True and (self.name == other.name or self.name == "")) else False
        result = True if (result is True and (self.second_name == other.second_name or self.second_name == "")) else False
        result = True if (result is True and (self.phone == other.phone or self.phone == "")) else False
        return result

    def __init__(self, surname: str, name: str, second_name: str, phone: str):
        self.__surname = surname
        self.__name = name
        self.__second_name = second_name
        self.__phone = phone

    # при прибавлении переменной класс к чему-то это что-то будет приклеено слева
    # сделал для добавления слева порядковых номеров контакта в телефонной книге
    def __radd__(self, other):
        return other + [self.surname, self.name, self.second_name, self.phone]

    # вывожу на печать типа красиво
    def __str__(self):
        return f'{self.surname} {self.name} {self.second_name}: {self.phone}'

    # получаю все значения в виде списка
    # сделал для удобства сохранения в файл
    def get(self):
        return self.surname, self.name, self.second_name, self.phone

    # геттеры
    def get_surname(self) -> str:
        return self.__surname

    def get_name(self) -> str:
        return self.__name

    def get_second_name(self) -> str:
        return self.__second_name

    def get_phone(self) -> str:
        return self.__phone

    def set_surname(self, surname: str) -> None:
        self.__surname = surname

    # сеттеры
    def set_name(self, name: str) -> None:
        self.__name = name

    def set_second_name(self, second_name: str) -> None:
        self.__second_name = second_name

    def set_phone(self, phone: str) -> None:
        self.__phone = phone

    # назначение геттеров и сеттеров
    surname = property(get_surname, set_surname)
    name = property(get_name, set_name)
    second_name = property(get_second_name, set_second_name)
    phone = property(get_phone, set_phone)
