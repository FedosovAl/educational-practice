# TODO здесь писать код
def input_data():
    text = input(f'{number}-я запись: ').split()
    digit = text[0]
    while len(text) != 2:
        print('Ошибка ввода. Запись должно состоять из 2 элементов:'
              ' имя участника(1 слово) и количества очков(целое число).')
        text = input(f'{number}-я запись: ').split()
    participants[f'{number}-я запись'] = tuple(text)


def find_number_of_participants(data, count_of_participants):
    for score, name in data.values():
        if data['1-я запись'][1] != name:
            count_of_participants += 1
    return count_of_participants


def location_determination(data):
    maximum_score = 0
    place = ''
    name = ''
    keys = []
    for key, meaning in data.items():
        points, nickname = meaning
        points = int(points)
        if points > maximum_score:
            maximum_score = points
            place = (nickname, points)
            name = nickname
    for key, meaning in data.items():
        points, nickname = meaning
        if name == nickname:
            keys.append(key)
    for element in keys:
        data.pop(element)
    return place


number_of_records = int(input('Сколько записей вносится в протокол? '))
participants = dict()
count = 0
# first_place = ''
# second_place = ''
# third_place = ''
for number in range(1, number_of_records + 1):
    input_data()
count = find_number_of_participants(participants, count)
while count < 3:
    print('Минимальное количество участникоов 3.')
    count = find_number_of_participants(participants, count)
first_place = location_determination(participants)
second_place = location_determination(participants)
third_place = location_determination(participants)
print('1-е место.', first_place)
print('2-е место.', second_place)
print('3-е место.', third_place)
