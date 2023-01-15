# TODO здесь писать код
import random

number_sticks = int(input('Количество палочек: '))
number_throws = int(input('Количество бросков: '))
sticks = ['|' for _ in range(number_sticks)]
for count in range(number_throws):
    print('Бросок', count + 1, end='. ')
    left_border = random.randint(1, 5)
    right_border = random.randint(5, 10)
    for element in range(left_border, right_border):
        sticks[element] = '.'
    print('Сбиты палки с номера', left_border, 'по номер', right_border)
print('\nРезультат: ', end='')
for stick in range(len(sticks)):
    print(sticks[stick], end='')
