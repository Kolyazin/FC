from contact import Contact
from phonebook import PhoneBook

print("Phone Book v2.0")

pb = PhoneBook()
tmp = Contact('Иванов', 'Иван', 'Иванович', '911')
pb.add_contact(tmp)
tmp = Contact('Петров', 'Петр', 'Петрович', '112')
pb.add_contact(tmp)
print(pb)
