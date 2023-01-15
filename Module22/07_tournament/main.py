# TODO здесь писать код
first_file = open('first_tour.txt', 'r', encoding='utf-8')
second_file = open('second_tour.txt', 'w', encoding='utf-8')
print('Содержимое файла first_tour.txt:')
passing_score = 0
elements = []
number_people = 0
number = 1
second_file.write('\n')
maximum_score = 0
for element in first_file:
    print(element, end='')
    elements = element.split()
    if len(elements) == 1:
        passing_score = int(elements[0])
    else:
        if int(elements[2]) > passing_score:
            number_people += 1
            maximum_score = int(elements[2])
            record = (str(number) + ')' + str(elements[1][:1]) + '.' + str(elements[0])
                                  + ' ' + str(elements[2]) + '\n')
            if int(elements[2]) > maximum_score:
                maximum_score = int(elements[2])
                second_file.seek(0)
                second_file.write(record)
                number += 1
            else:
                second_file.write(record)
                number += 1
second_file.seek(0)
second_file.write(str(number_people))
second_file.close()
first_file.close()
print('\n\nСодержимое файла second_tour.txt:')
second_file = open('second_tour.txt', 'r', encoding='utf-8')
text = second_file.read()
print(text)
