# TODO здесь писать код
from collections import Counter

if __name__ == "__main__":
    def can_be_poly(my_string: str) -> bool:
        """
        Функция определяет можно ли из переданной строки составить полиндром.

        :param: my_string(str) - передает строку
        :return:
            True если количество символов, которые встречаются в строке нечетное количество раз, не больше 2
            False  если количество символов, которые встречаются в строке нечетное количество раз, больше 2
        """
        return len(list(filter(lambda element: element % 2, Counter(my_string).values()))) <= 2


    print(can_be_poly('abcba'))
    print(can_be_poly('abbbc'))