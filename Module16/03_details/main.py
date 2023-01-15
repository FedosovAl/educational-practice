shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

# TODO здесь писать код

element_count = 0
price = 0
element_name = input('Введите название детали: ')
for element in range(len(shop)):
    if shop[element][0] == element_name:
        element_count += 1
        price += shop[element][1]
print('Количество деталей -', element_count)
print('Общая стоимость -', price)
