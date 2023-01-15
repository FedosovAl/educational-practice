# TODO здесь писать код
number_of_orderings = int(input('Количество заказов: '))
orderings = dict()
for number in range(1, number_of_orderings + 1):
    ordering = input(f'{number} - й заказа: ').split()
    name, pizza, count = ordering
    count = int(count)
    if name not in orderings:
        orderings[name] = {pizza: count}
    else:
        if pizza not in orderings[name]:
            orderings[name][pizza] = count
        else:
            orderings[name][pizza] += count
for element in orderings:
    print(f'{element}:')
    for component in orderings[element]:
        print(f'\t{component} : {orderings[element][component]}')
