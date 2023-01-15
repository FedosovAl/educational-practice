# TODO здесь писать код
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
message = input('Сообщение: ')
symbols_in_message = []
symbols_in_message.extend(message)
reverse_word = ''
word = []
reverse_message = []
for symbol in symbols_in_message:
    if symbol.lower() in alphabet:
        word.append(symbol)
    else:
        word.reverse()
        for element in word:
            reverse_word += element
        reverse_message.append(reverse_word)
        reverse_message.append(symbol)
        word = []
        reverse_word = ''
print('Новое сообщение:', end=' ')
for symbol in reverse_message:
    print(symbol, end='')