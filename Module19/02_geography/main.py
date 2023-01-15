# TODO здесь писать код
number_of_countries = int(input('Количество стран: '))
position = 1
country_and_cities = dict()
for number in range(1, number_of_countries + 1):
    text = input(f'{number} - я страна: ').split()
    while position != len(text):
        country_and_cities[text[len(text) - position]] = text[0]
        position += 1
    position = 1
for number in range(1, 4):
    city = input(f'{number} - й город: ' )
    if city in country_and_cities:
        print(f'Город {city} расположен в стране {country_and_cities[city]}.')
    else:
        print(f'По городу {city} данных нет.')