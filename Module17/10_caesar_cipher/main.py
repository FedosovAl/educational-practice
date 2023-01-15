# TODO здесь писать код

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

text = input('Введите строку: ').lower()
step = int(input('Введите сдвиг: '))
new_text = ''
for symbol in text:
    if symbol == ' ':
        new_text += ' '
    for element in range(len(alphabet)):
        if symbol == alphabet[element]:
            new_text += alphabet[(element + step) % 33]
print('Зашифрованное сообщение:', new_text)


# Придумал только такое решение.