# TODO здесь писать код
import math


class MyMath:
    """ Класс описывает математические операции """

    @classmethod
    def circle_length(cls, radius: int) -> float:
        """
        Находит длину окружности

        :param: radius(int) - передает радиус окружности
        :return: result(float) - возвращает длину окружности
        """
        result = 2 * math.pi * radius
        return result

    @classmethod
    def circle_square(cls, radius: int) -> float:
        """
        Находит площадь окружности

        :param: radius(int) - передает радиус окружности
        :return: result(float) - возвращает площадь окружности
        """
        result = math.pi * radius ** 2
        return result

    @classmethod
    def cube_volume(cls, length: int) -> float:
        """
        Находит объем куба

        :param: length(int) - передает длину стороны куба
        :return: result(float) - возвращает объем куба
        """
        result = length ** 3
        return result

    @classmethod
    def sphere_square(cls, radius: int) -> float:
        """
        Находит площадь поверхности сферы

        :param: radius(int) - передает радиус сферы
        :return: result(float) - возвращает площадь поверхности сферы
        """
        result = 4 * math.pi * radius ** 2
        return result


result_1 = round(MyMath.circle_length(5), 2)
result_2 = round(MyMath.circle_square(6), 2)
result_3 = round(MyMath.cube_volume(3), 2)
result_4 = round(MyMath.sphere_square(7), 2)
print('Длина окружности с радиусом 5 -', result_1)
print('Площадь окружности с радиусом 6 -', result_2)
print('Объем куба со стороной 3 -', result_1)
print('Площадь поверхности сферы с радиусом 7 -', result_2)
