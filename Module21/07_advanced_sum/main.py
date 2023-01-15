# TODO здесь писать код
def calculate_sum(x, numbers=None):
    if numbers is None:
        numbers = []
    for i in x:
        if isinstance(i, int):
            numbers.append(i)
        else:
            calculate_sum(i, numbers)
    return sum(numbers)


result = calculate_sum([[1, 2, [3]], [1], 3])
print('Сумма:', result)
