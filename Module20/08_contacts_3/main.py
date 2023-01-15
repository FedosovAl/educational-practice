# TODO здесь писать код

phone__book = dict()
while True:
    print('Введите номер действия: \n1. Добавить контакт \n2. Найти человека')
    action = int(input())
    if action == 1:
        person = input('Введите имя и фамилию нового контакта (через пробел): ').split()
        while tuple(person) in phone__book.keys():
            print('Такой человек уже есть в контактах.')
            print('Текущий словарь контактов:', phone__book)
            print('Введите номер действия: \n1. Добавить контакт \n2. Найти человека')
            action = int(input())
        number = int(input('Введите номер телефона:'))
        phone__book[tuple(person)] = number
        print('Текущий словарь контактов:', phone__book)
    elif action == 2:
        word = input('Введите фамилию для поиска: ')
        for people, number in phone__book.items():
            if word in people:
                name, surname = people
                print(name, surname, number)
                break
        else:
            print('Данных о человеке с такой фамилией нет.')
    else:
        print('Ошибка ввода. Нужно выбрать 1 или 2.')
