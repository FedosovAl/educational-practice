# TODO здесь писать код
import random

border = int(input('Введите длину списка: '))
numbers = [random.randint(1, 20) for _ in range(border)]
new_numbers = [(numbers[element] // numbers[element] if element % 2 == 0 else numbers[element] // 5)
               for element in range(len(numbers))]
print('Список чисел: ', new_numbers)
print('Результат: ', new_numbers)
