# TODO здесь писать код
import math


class Square:
    """
    Базовый класс описывает квадрат

    :param: _length(int) - передает длину стороны квадрата
    """

    def __init__(self, length: int) -> None:
        self._length = length

    def find_perimeter(self) -> int:
        """
        Находит периметр квадрата

        :return: result(int) - возвращает значение периметра квадрата
        """
        result = self._length * 4
        return result

    def find_square(self) -> int:
        """
        Находит площадь квадрата

        :return: result(int) - возвращает значение площади квадрата
        """
        result = self._length ** 2
        return result

    @property
    def length(self) -> int:
        """
        Геттер. Возвращает значение длины стороны
        :return: _length(int) - возвращает длину стороны квадрата
        """
        return self._length

    @length.setter
    def length(self, value: int) -> None:
        """
        Сеттер. Изменяет длину стороны квадрата на переданное значение
        :param: value(int) - передает новое значение длины
        """
        self._length = value


class Triangle:
    """
    Базовый класс описывает треугольник
    :param:
        _height(int) - передает высоту
        _footing(int) - передает длину основания
    """
    def __init__(self, height: int, footing: int) -> None:
        self._height = height
        self._footing = footing

    def find_perimeter(self) -> float:
        """
        Находит периметр треугольника

        :return: result(float) - возвращает значение площади треугольника
        """
        thigh = math.sqrt((self.footing / 2) ** 2 + self.height ** 2)
        result = self.footing + thigh * 2
        return result

    def find_square(self) -> float:
        """
        Находит площадь треугольника

        :return: result(int) - возвращает значение площади треугольника
        """
        result = self.height * self.footing * 0.5
        return result

    @property
    def height(self) -> int:
        """
        Геттер. Возвращает высоту
        :return: _height(int) - возвращает длину высоты
        """
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        """
        Сеттер. Изменяет высоту на переданное значение
        :param: value(int) - передает новое значение высоты
        """
        self._height = value

    @property
    def footing(self) -> int:
        """
        Геттер. Возвращает длину основания
        :return: _footing(int) - возвращает длину основания
        """
        return self._footing

    @footing.setter
    def footing(self, value: int) -> None:
        """
        Сеттер. Изменяет длину оснвоания на переданное значение
        :param: value(int) - передает новое значение длины основания
        """
        self._footing = value


class Cube(Square):
    """
    Класс описывает куб. Родитель Square
    :param: length(int) - передает дллину стороны
    """

    def __init__(self, length: int) -> None:
        super().__init__(length)

    @property
    def find_square(self) -> int:
        """
        Находит площадь поверхности куба
        :return: result(int) - возвращает площадь поверхности куба
        """
        result = super().find_square() * 6
        return result


class Pyramid(Triangle, Square):
    """
    Класс описывает пирамиду. Родители Triangle и Square
    :param:
        height(int) - передает высоту
        footing(int) - передает длину основания
    """

    def __init__(self, height: int, footing: int) -> None:
        super().__init__(height, footing)

    @property
    def find_square(self) -> int:
        """
        Находит площадь поверхности пирамиды
        :return: result(int) - возвращает площадь поверхности пирамиды
        """
        side_square = 4 * super().find_square()
        base_square = self.footing ** 2
        result = side_square + base_square
        return result


figure = Cube(5)
print('Площадь куба -', figure.find_square)

figure = Pyramid(6, 4)
print('Площадь пирамиды -', figure.find_square)


