# TODO здесь писать код

import random

# numbers = [random.randint(0, 10) for _ in range(10)]
# odd_index = []
# even_index = []
# result = []
# print('Оригинальный список:', numbers)
# for index, number in enumerate(numbers):
#     if index % 2 != 0:
#         odd_index.append(number)
#     else:
#         even_index.append(number)
# new_numbers = zip(even_index, odd_index)
# for element in new_numbers:
#     result.append(element)
# print('Новый список:', result)


numbers = [random.randint(0, 10) for _ in range(10)]
print('Оригинальный список:',numbers)
new_numbers = []
for index in range(0, len(numbers), 2):
    new_numbers.append((numbers[index], numbers[index + 1]))
print('Новый список:',new_numbers)
