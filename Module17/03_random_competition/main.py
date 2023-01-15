# TODO здесь писать код

import random

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
result = [(first_team[element] if first_team[element] > second_team[element] else second_team[element]) for element in range(20)]
print('Первая команда:', first_team)
print('Вторая команда:', second_team)
print('Победители тура:', result)
