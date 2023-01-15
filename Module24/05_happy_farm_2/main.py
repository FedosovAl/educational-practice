# TODO здесь писать код
class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]))


class PotatoGarden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for potato in self.potatoes:
            potato.grow()

    def are_all_ripe(self):
        if not all([potato.is_ripe() for potato in self.potatoes]):
            return False
        else:
            return True

    def print_all_states(self):
        for potato in self.potatoes:
            potato.print_state()


class Gardener:
    def __init__(self, name, collected_potatoes):
        self.name = name
        self.collected_potatoes = collected_potatoes

    def gardener_info(self):
        print('{} всего собрал {} картофелин!'.format(self.name, self.collected_potatoes))

    def tend(self, my_garden):
        if my_garden.are_all_ripe():
            print('Вся картошка созрела. Можно собирать!\n')
            question = int(input('Собрать картошку (1 - да, 2 - нет)? '))
            if question == 1:
                potato_count = 0
                for _ in my_garden.potatoes:
                    self.collected_potatoes += 1
                    potato_count += 1
                print('{} собрал {} картофелин!'.format(self.name, potato_count))
                self.gardener_info()
        else:
            print('Картошка ещё не созрела!\n')
            question = int(input('Отправить {}а ухаживать за картошкой (1 - да, 2 - нет)? '.format(self.name)))
            if question == 1:
                my_garden.grow_all()
                my_garden.are_all_ripe()


garden = PotatoGarden(5)
worker = Gardener('Василий', 0)
while True:
    worker.tend(garden)
    Potato.state = 0