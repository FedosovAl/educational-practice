# TODO здесь писать код
import math
import random


class Car:
    """
    Класс описывает автомобиль и его движение
    :args:
    coordinate_x (int) - передает координату 'x' положения автомобиля
    coordinate_y (int) - передает координату 'y' положения автомобиля
    angle_of_movement(int) - угол, описывающий направление движения
    attributes:
    coordinate_x (int): координата 'x' точки нахождения автомобиля
    y (int): координата 'y' точки нахождения автомобиля
    """
    def __init__(self, coordinate_x, coordinate_y, angle_of_movement):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.angle_of_movement = angle_of_movement

    def move(self, distance):
        """
        Вычисляет точку конечного следования автомобиля

        :param distance: передаётся дистанция на которую движется автомобиль
        :rtype: int

        :param angle_of_movement: передаётся угол направления движения автомобиля
        :rtype: int

        """
        self.coordinate_x = self.coordinate_x + distance * math.cos(self.angle_of_movement)
        self.coordinate_y = self.coordinate_y + distance * math.sin(self.angle_of_movement)


class Bus(Car):
    """
    Класс описывает положение автобуса, его движение, наполняемость пассавжирами и количество денег
    :args (int):
        passengers - количество пассажирова
        money - количество денег
    """
    __passengers = 0
    __money = 0

    def __init__(self, coordinate_x, coordinate_y, angle_of_movement):
        super().__init__(coordinate_x, coordinate_y, angle_of_movement)

    def enter(self, passengers_count):
        """
        Приавляет вощедших пассажиров к общему количеству пассажиров в автобусе, если автобус не заполнен,
        иначе выводит сообщение о заполненности

        :param passengers_count: количество вошедших пассажирова
        :type int
        """
        count = 0
        if self.__passengers < 45:
            for _ in range(passengers_count):
                count += 1
                self.__passengers += 1
                if self.__passengers == 45:
                    break
            print('Зашло {} пассажиров. В автобусе сейчас {} пассажирова'.format(passengers_count, self.__passengers))
        else:
            print('Автобус полностью заполнен, никто не зашел')

    def exit(self, passengers_count):
        """
        Вычитает выщедших пассажиров из общего количества пассажиров в автобусе, если пассажири в автобусе есть,
        иначе выводит сообщение об отсутсвии пассажиров

        :param passengers_count: количество вошедших пассажирова
        :type int
        """
        count = 0
        if self.__passengers > 0:
            for _ in range(passengers_count):
                count += 1
                self.__passengers -= 1
                if self.__passengers == 0:
                    break
            print('Вышло {} пассажиров. В автобусе сейчас {} пассажирова'.format(count, self.__passengers))
        else:
            print('Автобус пуст')

    def move(self, distance):
        """
        Изменение координат положения автомобиля в соответсвии с движением и считает заработанные деньги
        :param distance (int): пройденная дистанция
        """
        super().move(distance)
        self.__money += self.__passengers * 25 + distance
        print('\nПроехали {} метров. Заработано {}'.format(distance, self.__money))


car = Car(1, 2, 30)
bus = Bus(4, 5, 30)

route = 0
while route != 5:
    route += 1
    if random.randint(1, 2) == 2:
        bus.move(300)
        bus.enter(random.randint(1, 5))
        bus.exit(random.randint(1, 5))
    else:
        bus.move(random.randint(1, 300))
        bus.enter(random.randint(1, 5))
        bus.exit(random.randint(1, 5))
