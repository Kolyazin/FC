class Contact:
    def __init__(self, surname: str, name: str, second_name: str, phone: str):
        self.surname = surname
        self.name = name
        self.second_name = second_name
        self.phone = phone

    def __str__(self):
        return f'{self.surname} {self.name} {self.second_name}: {self.phone}'

    def get_surname(self) -> str:
        return self.surname

    def get_name(self) -> str:
        return self.name

    def get_second_name(self) -> str:
        return self.second_name

    def get_phone(self) -> str:
        return self.phone

    def set_surname(self, surname: str) -> None:
        self.surname = surname

    def set_name(self, name: str) -> None:
        self.name = name

    def set_second_name(self, second_name: str) -> None:
        self.second_name = second_name

    def set_phone(self, phone: str) -> None:
        self.phone = phone
