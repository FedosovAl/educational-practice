# TODO здесь писать код

class MyDict:
    """
    Класс словарь

    :arg my_dict (dict)
    """
    def __init__(self):
        self.my_dict = {'name': 'Vova', 'age': '28', 'city': 'Moscow', 'profession': 'programmer'}

    def print_my_dict(self):
        """
        Выводит словарь

        """
        for element, value in self.my_dict.items():
            print(element + ': ' + value)

    def get_my_dict(self, value):
        """
        Выводит значение искомого ключа, если ключе нет возвращает 0

        :param value (str): передает искомый ключ
        """
        print(self.my_dict.get(str(value), 0))


my_dict = MyDict()
my_dict.print_my_dict()
number = input('\nЗначение какого ключа получить? ')
my_dict.get_my_dict(number)