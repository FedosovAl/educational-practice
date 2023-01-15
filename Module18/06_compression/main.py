# TODO здесь писать код

text = input('Введите строку: ')
symbols = []
new_symbols = []
past_symbol = ''
for symbol in text:
    if past_symbol != symbol and symbols == []:
        symbols.append(symbol)
        past_symbol = symbol
    elif past_symbol == symbol:
        symbols.append(symbol)
    elif past_symbol != symbol and symbols != []:
        new_symbols.append(past_symbol)
        new_symbols.append(symbols.count(past_symbol))
        past_symbol = symbol
        symbols.clear()
        symbols.append(past_symbol)
new_symbols.append(past_symbol)
new_symbols.append(symbols.count(past_symbol))
print('Закодированная строка:', end='')
for element in new_symbols:
    print(element, end='')