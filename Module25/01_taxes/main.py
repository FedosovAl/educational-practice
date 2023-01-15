# TODO здесь писать код

class Property:
    """
    Базовый класс, описывающий имущество человека

    :arg worth (int): передает стоимость имущества
    """
    def __init__(self, worth):
        self.worth = worth

    def tax_calculation(self):
        """
        Расчитывает и возвращает стоимость налога

        :return: self.worth / 1
        :rtype: int
        """
        return self.worth / 1


class Apartment(Property):
    """
    Класс квартира. Родитель Property

    :arg worth (int): передает стоимость квартиры
    """
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        """
        Расчитывает и возвращает стоимость налога на квартиру

        :return: self.worth / 1000
        :rtype: int
        """
        return self.worth / 1000


class Car(Property):
    """
    Класс Машина. Родитель Property
    :arg worth (int): передает стоимость машины
    """
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        """
        Расчитывает и возвращает стоимость налога на машину

        :return: self.worth / 1000
        :rtype: int
        """
        return self.worth / 200


class CountryHouse(Property):
    """
        Класс Дача. Родитель Property
        :arg worth (int): передает стоимость дачи
        """
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        """
        Расчитывает и возвращает стоимость налога на дачу

        :return: self.worth / 1000
        :rtype: int
        """
        return self.worth / 500


money = int(input('Введите количество денег: '))
apartment_worth = int(input('Введите стоимость квартиры: '))
car_worth = int(input('Введите стоимость машины: '))
country_house_worth = int(input('Введите стоимость дачи: '))
apartment = Apartment(apartment_worth)
car = Car(car_worth)
country_house = CountryHouse(country_house_worth)
tax_apartment = apartment.tax_calculation()
tax_car = car.tax_calculation()
tax_country_house = country_house.tax_calculation()
print('Налог на квартиру: ', tax_apartment)
print('Налог на  машину: ', tax_car)
print('Налог на дачу: ', tax_country_house)
if money - tax_apartment - tax_car - tax_country_house >= 0:
    print('Денег хватает на оплату налогов')
else:
    extra_money = abs(money - tax_apartment - tax_car - tax_country_house)
    print('На оплату налогов не хватает:', extra_money)