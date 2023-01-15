# TODO здесь писать код
import os


def saving_text(user_text):
    user_path = input('\nКуда хотите сохранить документ? '
                      'Введите последовательность папок (через пробел): ').split()
    file_name = input('\nВведите имя файла: ')
    file_name = file_name + '.txt'
    path_to_save = ''
    ready_path = generate_path(user_path, path_to_save)
    if os.path.exists(ready_path):
        os.chdir(ready_path)
        if os.path.exists(file_name):
            answer = input('Вы действительно хоттите перезаписать файл? ').lower()
            if answer == 'да':
                file = open(file_name, 'w')
                file.write(user_text)
                file.close()
            else:
                saving_text(user_text)
        else:
            file = open(file_name, 'w')
            file.write(user_text)
            file.close()
    else:
        print('Указанный из папок путь не существует. Попробуйте еще раз.')
        saving_text(user_text)
    print('Файл успешно перезаписан!')
    print('\nСодержимое файла:')
    name = open(file_name, 'r', encoding='utf-8')
    file = name.read()
    print(file)
    name.close()


def generate_path(path, save):
    for element in path:
        save = os.path.abspath(os.path.join(os.path.sep, save, element))
    return save


text = input('Введите текст: ')
saving_text(text)

