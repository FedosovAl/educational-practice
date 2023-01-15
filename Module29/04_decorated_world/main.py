# TODO здесь писать код
import functools
from typing import Callable


def decorator_with_args_for_any_decorator(func: Callable) -> Callable:
    """
    Декоратор. Принимает от другого декоратора аргументы, которые передали в декорируемый декоратор.
    :param: func(Callable) - передает декорируемую функцию.
    :return: wrapper(Callable) - возвращает функцию-обертку
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        """
        Функция обертка, принимает аргументы от декорируемой функции, и возвращает объекта декорируемой
        функции.
        :param args: *args - принимает позиционные аргументы.
        :param kwargs: **kwargs - принимает именованные аргументы
        :return: func(Callable) - возвращает декоратор
        """
        print(f'Переданные арги и кварги в декоратор: {args}, {kwargs}')
        return func
    return wrapper


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable) -> Callable:
    """
    Декоратор. Принимает функцию и возвращает ее значение.
    :param: func(Callable) - передает функцию
    :return: wrapper(Callable) - возвращает функцию-обертку
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> str:
        """
        Функция-обертка. Возвращает результат работы декорируемой функции.
        :param args: *args - позиционные аргументы декорируемой функции.
        :param kwargs: **kwargs - именованные аргументы декорируемой функции.
        :return: result(str) - возвращает значение функции
        """
        result = func(*args, **kwargs)
        return result
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    """ Функция выводит сообщение с учетом переданных значений """
    print("Привет,", text, num)


decorated_function("Юзер", 101)
