# TODO здесь писать код

skates = []
people = []
coincidence = 0
skates_count = int(input('Количество коньков: '))
for count in range(skates_count):
    print('Размер ' + str(count + 1) + '-й ' + 'пары:', end=' ')
    skates_size = int(input())
    skates.append(skates_size)
people_count = int(input('\nКоличество людей: '))
for count in range(people_count):
    print('Размер ноги ' + str(count + 1) + '-го ' + 'человека:', end=' ')
    foot_size = int(input())
    people.append(foot_size)
for foot in people:
    for skate in skates:
        if foot == skate:
            skates.remove(skate)
            coincidence += 1
            break
    else:
        for skate in skates:
            minimum_size = min(skates)
            if foot < minimum_size:
                skates.remove(minimum_size)
                coincidence += 1
                break
print('\nНаибольшее кол-во людей, которые могут взять ролики:', coincidence)