# TODO здесь писать код
from typing import Callable
import functools


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор. Спрашивает у пользователя как дела перед выполнением функций.
    :param:  func(Callable) передает функцию
    :return: wrapped_func(Callable) возвращает функцию-обертку
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> str:
        answer = input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию')
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@how_are_you
def find_squares_of_numbers(number: int) -> None:
    """
    Находит и выводит на экран кваадраты всех чисел от 1 до number.
    :param: number(int) передает число, до которого выполняется функция
    """
    print('Квадраты всех чисел от 1 до {}'.format(number))
    for element in range(1, number + 1):
        print(element ** 2, end=' ')
    print('\n')


@how_are_you
def print_all_numbers(number: int) -> None:
    """
    Выводит на экран все числа от 1 до number.
    :param: number(int) передает число, до которого выполняется функция
    """
    print('Все числа от 1 до {}'.format(number))
    for element in range(1, number + 1):
        print(element, end=' ')
    print('\n')


print_all_numbers(10)
find_squares_of_numbers(10)
