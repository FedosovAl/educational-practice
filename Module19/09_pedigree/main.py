# TODO здесь писать код

number_of_people = int(input('Введите количество человек: '))
tree = dict()
levels = dict()
for number in range(1, number_of_people):
    pair = input(f'{number} - я пара: ').title().split()
    descendant, parent = pair
    tree[parent] = descendant
    levels[parent] = 0
    levels[descendant] = 0
    for element in tree:
        people = element
        while people in tree:
            people = tree[people]
            levels[element] += 1
print('\n“Высота” каждого члена семьи:')
for i in sorted(levels):
    print(i, levels[i])