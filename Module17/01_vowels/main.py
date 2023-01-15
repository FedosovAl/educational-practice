# TODO здесь писать код

text = input('Введите текст: ')
vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
vowels_in_text = []
vowels_count = [vowels_in_text.append(symbol) for symbol in text for element in vowels
                if symbol == element]
number_letters = len(vowels_in_text)
print('\nСписок гласных букв:', vowels_in_text)
print('Длина списка:', number_letters)
