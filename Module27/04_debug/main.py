# TODO здесь писать код
from typing import Callable, Any
from functools import wraps


def stringify_arg(arg: Any) -> str:
    if isinstance(arg, str):
        return f"'{arg}'"
    else:
        return str(arg)


def debug(func: Callable) -> Callable:
    """
    Декоратор для подсчета количества вызовов функции

    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """
        Функция - обертка для вывода числа вызова функций
        Мы используем глобальный параметр для хранения числа вызовов.

        :param args:
        :param kwargs:
        :return:
        """
        args_str = [stringify_arg(arg) for arg in args]
        kwargs_str = [f"{key}={stringify_arg(value)}" for key, value in kwargs.items()]
        all_args_str = ', '.join(args_str + kwargs_str)
        print(f'\nВызывается {func.__name__}({all_args_str})')
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' вернула '{result}'")
        print(result)
        return result
    return wrapper


@debug
def greeting(name: str, age: int = None) -> str:
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)