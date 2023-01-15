# TODO здесь писать код

import math

def calculate_and_output_number(number):
    expand_whole_part = ''
    whole_part = int(number)
    while whole_part != 0:
        digit = whole_part % 10
        expand_whole_part += str(digit)
        whole_part //= 10
    number_in_string = ''
    for symbol in reversed(str(number)):
        if symbol == '.':
            break
        number_in_string += symbol
    string = str(expand_whole_part) + '.' + number_in_string
    reversed_number = float(string)
    return reversed_number

first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))
first_reversed_number = calculate_and_output_number(first_number)
second_reversed_number = calculate_and_output_number(second_number)
summ = first_reversed_number + second_reversed_number
print('Сумма:', summ)

