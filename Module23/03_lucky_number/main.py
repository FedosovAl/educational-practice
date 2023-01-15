# TODO здесь писать код
import random

sum_numbers = 0
with open('out_file.txt', 'w') as file:
    try:
        while sum_numbers < 777:
            number = int(input('Введите число: '))
            chance = random.randint(1, 13)
            if chance == 13:
                raise Exception
            sum_numbers += number
            file.write(str(number) + '\n')
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
    except Exception:
        print('Вас постигла неудача!')
with open('out_file.txt', 'r') as text:
    print('\nСодержимое файла out_file.txt:')
    for element in text:
        print(element, end='')