# TODO здесь писать код
from typing import Callable
import functools
import time


def expectation(func: Callable) -> Callable:
    """
    Декоратор. Перед выполнением функции ждет несколько секунд .
    :param:  func(Callable) передает функцию
    :return: wrapped_func(Callable) возвращает функцию-обертку
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> str:
        print("Сейчас.")
        time.sleep(3)
        print("Через 3 секунды.")
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@expectation
def find_squares_of_numbers(number: int) -> None:
    """
    Находит и выводит на экран кваадраты всех чисел от 1 до number.
    :param: number(int) передает число, до которого выполняется функция
    """
    print('Квадраты всех чисел от 1 до {}'.format(number))
    for element in range(1, number + 1):
        print(element ** 2, end=' ')
    print('\n')


find_squares_of_numbers(5)
