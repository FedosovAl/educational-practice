# TODO здесь писать код
def input_numbers_from_1_to_number(number, start=1):
    if start != number:
        print(start)
        return input_numbers_from_1_to_number(number, start + 1)
    else:
        print(start)


value = int(input('Введите число: '))
input_numbers_from_1_to_number(value)