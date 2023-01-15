# TODO здесь писать код

numbers = open('numbers.txt', 'r')
answer = open('answer.txt', 'w')
summ = 0
print('Содержимое файла numbers.txt:')
for number in numbers:
    print(number, end='')
    for symbol in number:
        if symbol != ' ' and symbol != '\n':
            summ += int(number)
numbers.close()
answer.write(str(summ))
answer.close()
print('\nСодержимое файла answer.txt:')
answer = open('answer.txt', 'r')
result = answer.read()
print(result)
answer.close()