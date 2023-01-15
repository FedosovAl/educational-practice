# TODO здесь писать код
def calculate_prime_number(symbol):
    count = 0
    for number in range(2, symbol):
        if symbol % number == 0:
            count += 1
    if count > 0 or symbol == 0 or symbol == 1:
        return False
    else:
        return True


def making_list_by_indexes(text): return [
    element
    for index, element in enumerate(text)
    if calculate_prime_number(index)
]


print(making_list_by_indexes('О Дивный Новый мир!'))