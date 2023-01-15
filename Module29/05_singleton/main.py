# TODO здесь писать код
import functools


def singleton(cls):
    """
    Декоратор-синглтон. Позволяет создать только 1 инстанс класса.
    Все последующие инстансы будут равны первому инстансу.
    """
    @functools.wraps(cls)
    def wrapped():
        if cls.current_instance is None:
            instance = cls()
            cls.current_instance = instance
            return instance
        return cls.current_instance
    cls.current_instance = None
    return wrapped


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()


print(id(my_obj))
print(id(my_another_obj))


print(my_obj is my_another_obj)
