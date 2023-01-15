# TODO здесь писать код
import random


class Human:

    def __init__(self, name):
        self.name = name
        self.satiety = 10
        self.house = True

    def information(self):
        print('Сытость - {},продукты - {}, деньги - {}'.format(self.satiety, House.fridge, House.money))

    def eating(self):
        House.fridge -= 10
        self.satiety += 10
        print('{} ест, сытость {} еда {}'.format(self.name, self.satiety, House.fridge))

    def work(self):
        self.satiety -= 10
        House.money += 10
        print('{} работает, сытость {} деньги {}'.format(self.name, self.satiety, House.money))

    def play(self):
        self.satiety -= 10
        print('играет, сытость {}'.format(self.satiety))

    def go_to_the_store(self):
        House.fridge += 10
        House.money -= 10
        print('{} идет в магазин, еда {} деньги {}'.format(self.name, House.fridge, House.money))


class House:
    fridge = 50
    money = 0


def life(name):
    for count in range(1, 366):
        print('День {}'.format(count))
        number_cubes = random.randint(1, 6)
        name.information()
        if name.satiety < 0:
            print(f'К сожалению, {name} скончался ')
            break
        if name.satiety < 20 and House.fridge >= 10:
            name.eating()
        elif House.fridge < 10:
            name.go_to_the_store()
        elif House.money < 50:
            name.work()
        elif number_cubes == 1:
            name.work()
        elif number_cubes == 2:
            name.eating()
        else:
            name.play()
    print('\nВыжил\n')


first_human = Human('Вова')
second_human = Human('Дима')
life(first_human)
life(second_human)


