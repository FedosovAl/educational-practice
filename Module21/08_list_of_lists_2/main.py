nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

# TODO здесь писать код


def print_numbers(numbers, new):
    for number in numbers:
        if isinstance(number, list):
            print_numbers(number, new)
        else:
            new.append(number)
    return new


new_numbers = []
result = print_numbers(nice_list, new_numbers)
print('Ответ:', result)