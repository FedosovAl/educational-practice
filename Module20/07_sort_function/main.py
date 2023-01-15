# TODO здесь писать код

def sorting_and_output_numbers(numbers):
    print(numbers)
    for number in numbers:
        if not isinstance(number, int):
            return numbers
    else:
        numbers = sorted(numbers)
        return tuple(numbers)


print(sorting_and_output_numbers((6, 3, -1, 8, 4, 10, -5)))
