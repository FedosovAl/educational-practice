# TODO здесь писать код
from typing import Callable
import random
import functools
import datetime
log = dict()


def logging(func: Callable) -> Callable:
    """
    Декоратор. Записывает в словарь данные в формате название функции: документация.
    :param:  func(Callable) передает функцию
    :return: wrapped_func(Callable) возвращает функцию-обертку
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> None:
        log[func.__name__] = func.__doc__
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@logging
def find_squares_of_numbers(number: int) -> None:
    """
    Делит числа от 1 до number на случайное число от 0 до 2 и выводит результат деления.
    Если делитель равен 0 записывает ошибку в файл function_errors.log и продолжает работу программы.
    :param: number(int) передает число, до которого выполняется функция
    """

    with open('function_errors.log', 'w', encoding='utf-8') as file:
        for element in range(1, number + 1):
            try:
                divider = random.randint(0, 2)
                value = element / divider
                print('{} / {} = {}'.format(element, divider, value))
            except ZeroDivisionError as error:
                now = datetime.datetime.now()
                print('{} / 0 - на 0 делить нельзя'.format(element))
                file.write('{}: {} - {}\n'.format(
                    now,
                    str(find_squares_of_numbers.__name__),
                    str(error)))
                continue


result = find_squares_of_numbers(10)
print('\nНазвание и документация функции:')
for name, documents in log.items():
    print('{}:{}'.format(name, documents))