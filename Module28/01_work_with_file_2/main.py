# TODO здесь писать код
from typing import Self


class File:
    """
    Класс описывает открытие файла

    :param:
        name(str) - передает название файла
        mode(str) - передает режим чтения файла
    """

    def __init__(self, name: str, mode: str):
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self) -> Self:
        try:
            self.file = open(self.name, self.mode, encoding='utf-8')
        except FileNotFoundError:
            self.file = open(self.name, 'w', encoding='utf-8')
            print(f'Файл не найден. Файл {self.name} открыт для записи.')
            data = input('Что запишем в файл? ')
            self.file.write(data)
            print('Данные записаны.')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        return True


with File('Example.txt', 'r') as file:
    file = file.read()
    print(file)



