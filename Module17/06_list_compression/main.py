# TODO здесь писать код

import random

numbers_count = int(input('Количество чисел в списке: '))
numbers = [random.randint(0, 2) for _ in range(numbers_count)]
print('Список до сжатия: ', numbers)

for number in range(len(numbers)):
    for element in range(number, len(numbers)):
        if numbers[number] == 0:
            numbers[number], numbers[element] = numbers[element], numbers[number]
print('Список после перестановки:', numbers)
new_numbers = numbers[:]
for number in new_numbers:
    if number == 0:
        numbers.remove(number)
print('Список после сжатия:', numbers)

# Решил дополнительно вывести список после перестановки,
# т.к. в противном случае можно было бы просто удалить 0
# из списка и не переносить их в конец списка
