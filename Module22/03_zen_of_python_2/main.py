# TODO здесь писать код
import os
path_to_zen = os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt'))
zen = open(path_to_zen, 'r')
number_of_letters = 0
number_of_strings = 0
words = []
all_words = []
symbols = dict()
all_letters = ''
minimum_value = 999999999
minimum_key = ''
for string in zen:
    number_of_strings += 1
    words = string.split()
    for element in words:
        all_letters += element
        all_words.append(element)
    for symbol in string:
        symbol = symbol.lower()
        if symbol.isalpha():
            symbols[symbol] = all_letters.count(symbol)
        if symbol != ' ' and symbol != '\n':
            number_of_letters += 1
number_of_words = len(all_words) - 1
for key, value in symbols.items():
    if value < minimum_value:
        minimum = value
        minimum_key = key
print('Количество букв в файле:', number_of_letters)
print('Количество слов в файле:', number_of_words)
print('Количество строк в файле:', number_of_strings)
print('Наиболее редкая буква:', minimum_key)