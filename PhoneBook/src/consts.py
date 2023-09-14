from pathlib import Path

defaultBook = ['Иванов,Иван,Иванович,+71234567890',
               'Петров,Петр,Петрович,+70987654321',
               ]
booksFolder = Path(Path(__file__).parent, r'data')
txtBookFile = Path(booksFolder, r'pb.txt')
csvBookFile = Path(booksFolder, r'pb.csv')
