# TODO здесь писать код

zen = open('zen.txt', 'r')
text = []
for string in zen:
    text.append(string)
zen.close()
for element in text[::-1]:
    if element.endswith('\n'):
        print(element, end='')
    else:
        print(element)