# TODO здесь писать код

import random


class House:
    """
    Класс описывает дом. Базовый класс
    attributes:
    money (int): количество денег
    food (int): количество еды
    cat_food (int): количество еды для кота
    dirt (int): количество грязии
    """
    money = 100
    food = 50
    cat_food = 30
    dirt = 0


class Husband(House):
    """
    Класс описывает мужа. Родитель House

    attributes:
    satiety (int): уровень сытости
    happiness (int): уровень счастья
    """
    satiety = 30
    happiness = 100

    def __init__(self, name):
        super().__init__()
        self.name = name

    def pet_the_cat(self):
        """
        Гладит кота, повышается уровень счастья и тратится сытость, после выводится сообщение на экран.
        """
        self.happiness += 5
        self.satiety -= 10
        print('{} погладил кота. Уровень счастья {}, сытость {}'.format(self.name, self.happiness, self.satiety))

    def eating(self):
        """
        Ест. Уровень сытости повышается на слуйчайное значение от 10 до 30 если еды больше 30,
        иначе уровень сытости повышается на 10

        :return: food_count (int) количество съеденной еды
        """
        food_count = random.randint(10, 30) if House.food > 30 else 10
        if food_count > House.food:
            self.satiety += House.food
            House.food = 0
        else:
            self.satiety += food_count
            House.food -= food_count
        return food_count

    def play(self):
        """
        Играет. Уменьшается количество сытости, повышается уровень счастья.
        После выводится сообщение на экран.
        """
        self.satiety -= 10
        self.happiness += 20
        print('{} поиграл. Сытость {}, уровень счастья {}'.format(self.name, self.satiety, self.happiness))

    def working(self):
        """
        Работает. Уменьшается количество сытости, повышается количество денег.
        После выводится сообщение на экран.
        """
        self.satiety -= 10
        House.money += 150
        print('{} поработал. Сытость {}, всего денег {}'.format(self.name, self.satiety, House.money))


class Wife(Husband):
    """
    Класс описывает жену. Родитель Husband.
    """
    def __init__(self, name):
        super().__init__(name)

    def buy_products(self):
        """
        Покупает продукты. Количество еды увеличивается на 30, если денег больше 30.
        Иначе количество продуктов равно случайному числу от 5 до количества денег.
        Еда для коты увеличивается на случайное число от 5 до 15.
        Увеличивается количество еды и количество еды для кота. Уменьшаются деньги.
        Уменьшается уровень сытости. Затем вывод сообщения.
        :return:
        """
        self.satiety -= 10
        food_count = 30 if House.money > 30 else random.randint(5, House.money)
        cat_food_count = random.randint(5, 15)
        House.cat_food += cat_food_count
        House.food += food_count
        House.money -= (food_count + cat_food_count)
        print('{} купила продукты. Сытость {}, еды {}, еда для кота {}, денег осталось {}'.format(
            self.name,
            self.satiety,
            House.food,
            House.cat_food,
            House.money))

    def buy_fur_coat(self):
        """
        Покупает шубу.

        Уменьшается количество сытости. Уменьшается количество денег. Увеличивается уровень счастья.
        Затем вывод сообщения.
        """
        self.satiety -= 10
        House.money -= 350
        self.happiness += 60
        print('{} купила шубу. Сытость {}, денег осталось {}, уровень счастья {}'.format(
            self.name,
            self.satiety,
            self.happiness,
            House.money))

    def cleaning_the_house(self):
        """
        Убирает дом.

        Уменьшается уровень сытости. Уменьшается грязь в доме. Если в результате количество грязи меньше 0,
        то значение грязи обнуляется.
        Затем вывод сообщения.
        """
        self.satiety -= 10
        House.dirt -= random.randint(1, 100)
        if House.dirt < 0:
            House.dirt = 0
        print('{} убрала дом. Сытость {}, чистота {}'.format(
            self.name,
            self.satiety,
            House.dirt))


class Cat(House):
    """
    Класс описывает кота. Родитель House
    attributes: satiety (int) уровень сытости
    """
    satiety = 30

    def __init__(self, name):
        super().__init__()
        self.name = name

    def eating(self):
        """
        Ест.
        Уровень сытости увеличивается на случайное значенние от 1 до 10. Если случайное значение
        больше количества еды, то уровень сытости увеличивается на количество еды, а еда обнуляется.
        Количество сытости уменьшается. ЗАтем вывод сообщения.
        """
        food_count = random.randint(1, 10)
        if food_count > House.cat_food:
            self.satiety += House.cat_food
            House.cat_food = 0
        self.satiety += food_count * 2
        House.cat_food -= food_count
        print('{} поел. Сытость кота {}, еды для кота осталось {}'.format(self.name, self.satiety, House.cat_food))

    def sleep(self):
        """
        Спит.
        Количество сытости уменьшается. ЗАтем вывод сообщения.
        """
        self.satiety -= 10
        print('{} поспал. Сытость кота {}'.format(self.name, self.satiety))

    def strip_the_wallpaper(self):
        """
        Дерет обои
        Увеличивается количество грязи. Уменьшается сытость. Затем вывод сообщения.
        """
        self.satiety -= 10
        House.dirt += 5
        print('{} подрал обои. Сытость кота {}, чистота {}'.format(self.name, self.satiety, House.dirt))


house = House()
husband = Husband('Николай')
wife = Wife('Елена')
cat = Cat('Маркиз')
day = 1
money = 0
food = 0
fur_coat = 0
print('\nДень {}\n'.format(day))
husband.working()
wife.cleaning_the_house()
cat.strip_the_wallpaper()
while day < 365:
    day += 1
    if (husband.satiety or wife.satiety or cat.satiety) < 0:
        print('Кто-то умер')
        break
    print('\nДень {}\n'.format(day))
    house.dirt += 5
    if house.food < 15 or house.cat_food < 15:
        wife.buy_products()
    elif wife.satiety <= 20:
        eaten = wife.eating()
        food += eaten
        print('Елена поела. Сытость {}, еды осталось {}'.format( wife.satiety, House.food))
    elif house.dirt >= 90:
        husband.happiness -= 10
        wife.happiness -= 10
        wife.cleaning_the_house()
    elif house.money > 350:
        wife.buy_fur_coat()
        fur_coat += 1
    else:
        wife.pet_the_cat()
    if husband.satiety <= 20:
        eaten = husband.eating()
        food += eaten
        print('Николай поел. Сытость {}, еды осталось {}'.format(husband.satiety, House.food))
    elif house.money < 400:
        husband.working()
        money += House.money
    else:
        husband.play()
        money += House.money
    if cat.satiety < 15:
        cat.eating()
    else:
        cat.strip_the_wallpaper()

print('\nИтоги за год:\nЗаработано денег - {}, съедено еды - {}, куплено шуб - {}'.format(money, food, fur_coat))