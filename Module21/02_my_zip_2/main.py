# TODO здесь писать код
def calculate_generator(first_data, second_data):
    first_values = sorted([element for element in first_data])
    second_values = sorted([element for element in second_data])
    border = min(len(first_values), len(second_values))
    x = ((first_values[value], second_values[value]) for value in range(border))
    return x


# result = calculate_generator('abcd', {1:0, 2:0, 3:0, 4:0})
# for i in result:
#     print(i)
