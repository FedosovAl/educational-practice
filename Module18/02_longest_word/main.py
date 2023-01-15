# TODO здесь писать код

text = input('Введите строку: ').split()
maximum_word = ''
maximum_lengh = 0

for word in text:
    if len(word) > len(maximum_word):
        maximum_word = word
        maximum_lengh = len(word)
print('Самое длинное слово:', maximum_word)
print('Длина этого слова:', maximum_lengh)



