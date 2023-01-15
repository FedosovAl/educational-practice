# TODO здесь писать код
import random


class Parent:
    children = []

    def __init__(self, parent_name, parent_age):
        self.parent_name = parent_name
        self.parent_age = parent_age

    def print_information(self):
        print('Меня зовут {}. Мне {} лет. Мои дети:'.format(self.parent_name, self.parent_age), end=' ')
        for element in self.children:
            print(element, end=' ')
        print()

    def calm_the_child_down(self):
        Child.calmness = True

    def feed_the_baby(self):
        Child.calmness = False


class Child:
    calmness = random.choice([True, False])
    hunger = random.choice([True, False])

    def __init__(self, child_name, child_age,
                 ):
        self.child_name = child_name
        self.child_age = child_age
        Parent.children.append(self.child_name)

    def state_of_calm(self):
        if self.calmness:
            print('Ребенок спокоен')
        else:
            print('Ребенок чем-то обеспокоен')
            answer = input('Хотите успокоить ребенка? ').lower()
            if answer == 'да':
                Parent.feed_the_baby(self.calmness)
                print('Теперь ребенок спокоен')

    def state_of_hunger(self):
        if self.hunger:
            print('Ребенок голоден')
            answer = input('Хотите покормить ребенка? ').lower()
            if answer == 'да':
                Parent.calm_the_child_down(self.hunger)
                print('Теперь ребенок сыт.')
        else:
            print('Ребенок не голоден')


parent_data = input('Введите имя и возраст родителя: ').split()
child_data = input('Введите имя и возраст ребенка: ').split()
while int(parent_data[1]) - int(child_data[1]) < 16:
    print('Возраст ребенка должен быть мменьше возраста родителя хотя бы на 16 лет')
    child_data = input('Введите имя и возраст ребенка: ').split()
parent = Parent(parent_data[0], int(parent_data[1]))
child = Child(child_data[0], int(child_data[1]))
parent.print_information()
child.state_of_calm()
child.state_of_hunger()

