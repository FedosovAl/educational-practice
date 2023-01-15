# TODO здесь писать код
from typing import Callable
import functools

count = []


def counter(func: Callable) -> Callable:
    """
    Декоратор. Считает и выводит количество вызовов функции .
    :param:  func(Callable) передает функцию
    :return: wrapped_func(Callable) возвращает функцию-обертку
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> str:
        result = func(*args, **kwargs)
        count.append('+')
        print('Функция вызвалась {}-й раз\n'.format(len(count)))
        return result
    return wrapped_func


@counter
def find_squares_of_numbers(number: int) -> None:
    """
    Находит и выводит на экран кваадраты всех чисел от 1 до number.
    :param: number(int) передает число, до которого выполняется функция
    """
    print('Квадраты всех чисел от 1 до {}'.format(number))
    for element in range(1, number + 1):
        print(element ** 2, end=' ')
    print('')


find_squares_of_numbers(5)
find_squares_of_numbers(15)
find_squares_of_numbers(25)
