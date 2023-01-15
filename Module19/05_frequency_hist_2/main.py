# TODO здесь писать код
text = input('Введите текст: ')
unique_symbols = set(text)
number_of_unique_symbols = dict()
inverted_dict = dict()
print('Оригинальный словарь частот:')
for symbol in sorted(unique_symbols):
    number_of_unique_symbols[symbol] = text.count(symbol)
    print(symbol, ':', number_of_unique_symbols[symbol])
print('\nИнвертированный словарь частот:')
for element in set(number_of_unique_symbols.values()):
    inverted_dict[element] = []
    for value in sorted(number_of_unique_symbols.keys()):
        if number_of_unique_symbols[value] == element:
            inverted_dict[element].append(value)
    print(element, ':', inverted_dict[element])
