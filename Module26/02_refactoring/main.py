# list_1 = [2, 5, 7, 10]
# list_2 = [3, 8, 4, 9]
# to_find = 56
#
# can_continue = True
# for x in list_1:
#     for y in list_2:
#         result = x * y
#         print(x, y, result)
#         if result == to_find:
#             print('Found!!!')
#             can_continue = False
#             break
#     if not can_continue:
#         break

# TODO провести рефакторинг кода
from collections.abc import Iterator


def find_value(numbers_1: list, numbers_2: list) -> Iterator[int]:
    """
    Вычисляет произведения чисел из списков
    :param numbers_1 (list): передает первый список чисел
    :param numbers_2 (list): передает второй список чисел
    :return: result (int) произведение чисел
    """
    for number in numbers_1:
        for element in numbers_2:
            result = number * element
            print('{} * {} = {}'.format(number, element, result))
            yield result


first_numbers = [2, 5, 7, 10]
second_numbers = [3, 8, 4, 9]
all_values = find_value(first_numbers, second_numbers)
print('Need to find 56')
print('Found!!!' if 56 in all_values else 'Not found')