# TODO здесь писать код
def errors():
    try:
        raise BaseException
    except BaseException:
        print('Ошибка: менее трёх символов в строке {}.'.format(line_count))


with open('people.txt', 'r', encoding='utf-8') as text:
    print('Содержимое файла people.txt:')
    for element in text:
        element = element.rstrip()
        print(element)
print()
with open('people.txt', 'r', encoding='utf-8') as text:
    symbols_count = 0
    line_count = 0
    for line in text:
        line_count += 1
        clean_line = line.rstrip()
        symbols_count += len(clean_line)
        if len(clean_line) < 3:
            errors()
    print('\nОбщее количество символов:', symbols_count)