# TODO здесь писать код

text = input('Введите строку: ')
string = set(text)
symbols = dict()
count = 0
for element in string:
    symbols[element] = text.count(element)
for value in symbols.values():
    if value % 2 != 0:
        count += 1
if count <= 1:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')