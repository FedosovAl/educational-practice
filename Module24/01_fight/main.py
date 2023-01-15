# TODO здесь писать код

import random


class Warrior:
    def __init__(self):
        self.first_health = 100
        self.second_health = 100

    def hit(self):
        if random.randint(1, 2) == 1:
            self.second_health -= 20
            print('Воин 1 бъет воина 2. У воина 2 осталось {} здоровья'.format(self.second_health))
        else:
            self.first_health -= 20
            print('Воин 2 бъет воина 1. У воина 1 осталось {} здоровья'.format(self.first_health))

    def battle(self):
        while (self.first_health or self.second_health) > 0:
            self.hit()
            if self.first_health == 0:
                print('Битва закончена. Победил воин 2')
                break
            elif self.second_health == 0:
                print('Битва закончена. Победил воин 1')
                break


bat = Warrior()
bat.battle()
