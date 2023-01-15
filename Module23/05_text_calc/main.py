# TODO здесь писать код
def errors():
    try:
        raise ValueError
    except ValueError:
        print('Ошибка в строке {}'.format(string), end='. ')


with open('calc.txt', 'r') as text:
    result = 0
    for string in text:
        data = string.split()
        if data[1] == '+':
            calculation = int(data[0]) + int(data[2])
            result += calculation
        elif data[1] == '-':
            calculation = int(data[0]) - int(data[2])
            result += calculation
        elif data[1] == '*':
            calculation = int(data[0]) * int(data[2])
            result += calculation
        elif data[1] == '/':
            calculation = int(data[0]) / int(data[2])
            result += calculation
        elif data[1] == '//':
            calculation = int(data[0]) // int(data[2])
            result += calculation
        elif data[1] == '%':
            calculation = int(data[0]) % int(data[2])
            result += calculation
        elif data[1] == '**':
            calculation = int(data[0]) % int(data[2])
            result += calculation
        else:
            string = string.rstrip()
            errors()
            answer = input('Хотите исправить? ').lower()
            if answer == 'да':
                new_string = input('Введите исправленную строку: ')
                with open('calc.txt', 'a') as new_text:
                    new_text.write('\n' + new_string)
result = round(result, 2)
print('\nСумма результатов:', result)