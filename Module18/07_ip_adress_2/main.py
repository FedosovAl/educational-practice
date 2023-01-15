# TODO здесь писать код

address = input('Введите IP: ').split('.')
print(address)
for element in address:
    if element.isdigit():
        if int(element) > 255:
            print(int(element), 'превышает 255.')
    elif element.startswith('-'):
        print(int(element), 'меньше 0.')
    elif element.isalnum():
        print(element, '- это не целое число')
    else:
        print('Адрес — это четыре числа, разделённые точками.')