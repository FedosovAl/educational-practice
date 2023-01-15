# TODO здесь писать код

class Water:

    def __init__(self):
        self.water = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()


class Air:

    def __init__(self):
        self.air = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()


class Earth:

    def __init__(self):
        self.earth = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()


class Fire:
    def __init__(self):
        self.fire = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()


class Storm():
    storm = 'Шторм'


class Steam:
    steam = 'Пар'


class Dirt:
    dirt = 'Грязь'


class Lightning:
    lightning = 'Молния'


class Dust:
    dust = 'Пыль'


class Lava:
    lava = 'Лава'


class Ether:
    ether = 'Эфир'


water = Water()
air = Air()
earth = Earth()
fire = Fire()
storm = water + air
print('{} + {} = {}'.format(water.water, air.air, storm.storm))
steam = water + fire
print('{} + {} = {}'.format(water.water, fire.fire, steam.steam))
dirt = water + earth
print('{} + {} = {}'.format(water.water, earth.earth, dirt.dirt))
lightning = air + fire
print('{} + {} = {}'.format(air.air, fire.fire, lightning.lightning))
dust = air + earth
print('{} + {} = {}'.format(air.air, earth.earth, dust.dust))
lava = fire + earth
print('{} + {} = {}'.format(fire.fire, earth.earth, lava.lava))
