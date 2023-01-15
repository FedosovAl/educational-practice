# TODO здесь писать код
import os
from collections.abc import Iterator


def gen_files_path(path: str) -> Iterator[str]:
    """
    Генерирует пути ко всем файлам в переданном каталоге
    :param: path(str) передает путь к каталогу
    :return: возвращает путь к файлу или папке
    """
    for root, folders, files in os.walk(path):
        for folder in folders:
            folder_path = os.path.join(root, folder)
            yield folder_path
        for file in files:
            file_path = os.path.join(root, file)
            yield file_path


user_path= input('Введите путь к каталогу: ')
while not os.path.exists(user_path):
    print('Такой директории не существует. Попробуйте еще раз.')
    user_path = input('Введите путь к каталогу: ')
folder_name = input('Введите название каталога: ')
new_path = os.path.join(user_path, folder_name)
while not os.path.exists(new_path):
    print('Такого каталога нет в этой директории. Попробуйте еще раз.')
    folder_name = input('Введите название каталога: ')
    new_path = os.path.join(user_path, folder_name)
default = os.path.abspath(os.path.join(os.sep))
catalog = gen_files_path(new_path)
print('Пути ко всем файлам в каталоге:\n')
for elem in catalog:
    print(elem)
