# TODO здесь писать код
maximum_number = int(input('Введите максимальное число: '))
result = {number for number in range(1, maximum_number + 1)}
while True:
    question = input('Нужное число есть среди вот этих чисел: ').lower()
    if question == 'помогите':
        break
    numbers = {int(number) for number in question.split()}
    answer = input('Ответ Артёма: ').lower()
    if answer == 'нет':
        result -= numbers
    else:
        result &= numbers
print('Артём мог загадать следующие числа:', end=' ')
for element in result:
    print(element, end=' ')
