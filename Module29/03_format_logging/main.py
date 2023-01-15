# TODO здесь писать код
from typing import Callable
import functools
from datetime import datetime
import time


def timer(date_format: str, cls, func: Callable) -> Callable:
    """ Декоратор. Выводит дату и время запуска метода, а также время работы метода."""
    for element in date_format:
        if element.isalpha():
            date_format = date_format.replace(element, '%' + element)

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        start = time.time()
        print(f"Запускается '{cls.__name__}.{func.__name__}'. Дата и время запуска: "
              f"{datetime.utcnow().strftime(date_format)}")
        result = func(*args, **kwargs)
        print(f'Тут метод {func.__name__}')
        end = time.time()
        print(f"\nЗавершение '{cls.__name__}.{func.__name__}', время работы = {round(end - start, 3)}s.")
        return result
    return wrapped_func


def log_methods(date_format) -> Callable:
    """ Декоратор. Применяет декоратор timer ко всем методам в классе. """
    @functools.wraps(date_format)
    def decorate(cls):
        for method_name in dir(cls):
            if method_name.startswith('__') is False:
                method = getattr(cls, method_name)
                decorate_method = timer(date_format, cls, method)
                setattr(cls, method_name, decorate_method)
        return cls
    return decorate


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()



