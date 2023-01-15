# TODO здесь писать код
from typing import Callable
import functools

app = dict()


def callback(value: str = None) -> Callable:
    def decorator_callback(func: Callable) -> Callable:
        """ Декоратор функции обратного вызова """
        app[value] = func

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_callback


@callback('//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

