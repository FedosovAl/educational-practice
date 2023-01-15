# TODO здесь писать код
import os
from collections.abc import Iterator


def all_python_files(path: str) -> Iterator[str]:
    """
    Находит строку кода в файлах .py, которые не являются пустыми или коментариями
    :param: path (str) передает путь к директории
    :return: возвращает строку с кодом
    """
    for root, folders, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                with open(file, 'r', encoding='utf-8') as file:
                    for line in file:
                        if not line.startswith('"') and not line.startswith('#') and line != '\n':
                            yield line


user_path = input('Введите путь к каталогу: ')
while not os.path.exists(user_path):
    print('Такой директории не существует. Попробуйте еще раз.')
    user_path = input('Введите путь к каталогу: ')
files = all_python_files(user_path)
line_count = 0
for elem in files:
    line_count += 1
print('Всего строк кода во всех файлах .py -', line_count)
