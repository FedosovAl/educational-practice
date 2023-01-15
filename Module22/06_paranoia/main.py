# TODO здесь писать код
alphabet_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_eng = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
word = ''
new_file = open('cipher_text.txt', 'w', encoding='utf-8')
name = open('text.txt', 'r', encoding='utf-8')
text = name.read()
step = 1
for element in text:
    if element in alphabet_eng:
        position = alphabet_eng.index(element) + step
        if position < len(alphabet_eng):
            word += alphabet_eng[position]
        else:
            new_position = abs(len(alphabet_eng) - position)
            word += alphabet_eng[new_position]
    elif element in alphabet_rus:
        position = alphabet_rus.index(element) + step
        if position < len(alphabet_rus):
            word += alphabet_rus[position]
        else:
            new_position = abs(len(alphabet_rus) - position)
            word += alphabet_rus[new_position]
    else:
        new_file.write(word + '\n')
        step += 1
        word = ''
new_file.write(word + '\n')
new_file.close()