# TODO здесь писать код
from typing import Callable
user_permissions = ['admin']
import functools


def check_permission(name: str) -> Callable:
    """
    Декоратор. проверяет, есть ли у пользователя доступ к вызываемой функции.
    :param: name(str) - gпередает имя пользователя
    :return: decorator(Callable) - возвращает декоратор
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> str:
            try:
                for element in user_permissions:
                    if name == element:
                        result = func(*args, **kwargs)
                        return result
                    else:
                        raise PermissionError('PermissionError')
            except PermissionError as error:
                print(f'{error}: У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')

        return wrapped_func
    return decorator


@check_permission('admin')
def delete_site() -> None:
    """ Вывод сообщения """
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment() -> None:
    """ Вывод сообщения """
    print('Добавляем комментарий')


delete_site()
add_comment()
