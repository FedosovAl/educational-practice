# TODO здесь писать код

first_list = []
second_list = []
for first_count in range(3):
    print('Введите', first_count + 1, 'число для 1 списка:', end=' ')
    number = int(input())
    first_list.append(number)
for second_count in range(7):
    print('Введите', second_count + 1, 'число для 2 списка:', end=' ')
    number = int(input())
    second_list.append(number)
print('\nПервый список:', first_list)
print('Второй список:', second_list)
first_list.extend(second_list)
for _ in range(len(first_list)):
    for element in first_list:
        if first_list.count(element) > 1:
            first_list.remove(element)
print('\nНовый первый список с уникальными элементами:', first_list)

# Не смог придумать решение без использования условного оператора