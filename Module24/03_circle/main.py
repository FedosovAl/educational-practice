# TODO здесь писать код
import math


class Circle:

    def __init__(self, coordinate_x=0, coordinate_y=0, radius=1):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.radius = radius

    def calculation_circle_square(self):
        square = round((math.pi * (self.radius ** 2)), 2)
        print('Площадь окружности:', square)

    def calculate_circle_perimeter(self):
        perimeter = round((2 * math.pi * self.radius), 2)
        print('Периметр окружности:', perimeter)

    def enlarge_circle(self, coefficient):
        new_radius = self.radius * coefficient
        print('Радиус увеличенной окружности в {} раз:'.format(coefficient), new_radius)

    def find_intersection(self, other_coordinate_x, other_coordinate_y, other_radius):
        dist = ((self.coordinate_x - int(other_coordinate_x)) ** 2 +
                (self.coordinate_y - int(other_coordinate_y)) ** 2) ** 0.5
        if abs(self.radius - int(other_radius)) <= dist <= self.radius + int(other_radius):
            return print('Окружности пересекаются')
        else:
            return print('Окружности не пересекаются')


circle_data = input('Введите координаты х и у, и радиус окружности через пробел: ').split()
circle = Circle(int(circle_data[0]), int(circle_data[1]), int(circle_data[2]))
circle.calculation_circle_square()
circle.calculate_circle_perimeter()
coefficient_magnification = int(input('Во сколько раз увеличить окружность: '))
circle.enlarge_circle(coefficient_magnification)
other_circle = input('Введите координаты х и у, и радиус другой окружности '
                     'через пробел для проверки их пересечения: ').split()
circle.find_intersection(other_circle[0], other_circle[1], other_circle[2])

