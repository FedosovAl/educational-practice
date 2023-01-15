# TODO здесь писать код
first_class = list(range(160, 178, 2))
second_class = list(range(162, 183, 3))
first_class.extend(second_class)
for current_element in range(len(first_class)):
    for element in range(current_element, len(first_class)):
        if first_class[element] < first_class[current_element]:
            first_class[element], first_class[current_element] = first_class[current_element], first_class[element]
print(first_class)