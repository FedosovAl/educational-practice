# TODO здесь писать код
import os


def find_file(path_to_element, number_elements=None):
    for element in os.listdir(path_to_element):
        new_path = os.path.join(path_to_element, element)
        if os.path.isfile(new_path):
            number_elements[0] += 1
            number_elements[2] += os.path.getsize(new_path)
        else:
            new_path = os.path.join(path_to_element, element)
            find_file(new_path, number_elements)
            number_elements[1] += 1
    return number_elements[0], number_elements[1], number_elements[2]


path = input('Введите путь: ')
abs_path = os.path.abspath(path)
number_files, number_dirs, size = find_file(abs_path, number_elements=[0, 0, 0])
new_size = round((size / 1024), 2)
print('Количество файлов:', number_files)
print('Количество подкаталогов:', number_dirs)
print('Размер каталога (в Кб):', new_size)
