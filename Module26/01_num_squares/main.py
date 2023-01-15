# TODO здесь писать код
from collections.abc import Iterator


class CalculateSquares:
    """
    Класс описывает вычисление квадратов чисел
    """

    def __init__(self, stop: int):
        self.start = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start > self.stop:
            raise StopIteration
        else:
            result = self.start ** 2
            return result


def calculate_squares(num: int) -> Iterator[int]:
    """
    Функция вычисляет квадраты чисел
    :param: num (int) передает число
    :return: result (int) возвращает число в квадрате
    """
    for elem in range(1, num + 1):
        result = elem ** 2
        yield result


number = int(input('Введите число: '))
numbers = CalculateSquares(number)
print('Последовательность квадратов чисел, полученная итераторорм:')
for element in numbers:
    print(element, end=' ')
print('\n\nПоследовательность квадратов чисел, полученная генераторорм:')
squares = calculate_squares(number)
for element in squares:
    print(element, end=' ')
print('\n\nПоследовательность квадратов чисел, полученная генераторным выражением:')
squares_gen = (element ** 2 for element in range(1, number + 1))
for element in squares_gen:
    print(element, end=' ')