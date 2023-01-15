# TODO здесь писать код

count_number = int(input('Кол-вл чисел: '))
numbers = []
for _ in range(count_number):
    number = int(input('Число: '))
    numbers.append(number)
print('Последовательность:', numbers)
new_numbers = []
reverse_list = []
result = []
for element in range(len(numbers)):
    for num in range(element, len(numbers)):
        new_numbers.append(numbers[num])
    reverse_list.extend(new_numbers)
    reverse_list.reverse()
    if new_numbers == reverse_list:
        for count_result in range(element):
            result.append(numbers[count_result])
        result.reverse()
        break
    new_numbers = []
    reverse_list = []
print('Нужно приписать чисел:', len(result))
print('Сами числа:', result)