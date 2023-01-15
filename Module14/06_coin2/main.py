# TODO здесь писать код
print('Введите координаты монетки:')
first_coordinate = float(input('X: '))
second_coordinate = float(input('Y: '))
radius = float(input('Введите радиус: '))
check_coordinate = (first_coordinate * first_coordinate + second_coordinate * second_coordinate) ** 0.5
if check_coordinate < radius:
    print('Монетка где-то рядом.')
else:
    print('Монетки в области нет')