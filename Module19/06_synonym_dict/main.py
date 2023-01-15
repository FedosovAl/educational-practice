# TODO здесь писать код
def creating_pairs(words):
    for component in words:
        if not component.isalpha():
            words.remove(component)
    return words


number_of_pairs = int(input('Количество пар слов: '))
synonyms = dict()
for number in range(1, number_of_pairs + 1):
    pair = input(f'{number} - я пара: ').lower().split()
    creating_pairs(pair)
    while len(pair) > 2:
        print('Ошибка. Синонимом не может быть больше 2.')
        pair = input(f'{number} - я пара: ').lower().split()
        creating_pairs(pair)
    synonyms[pair[0]] = pair[1]
word = input('\nВведите слово: ').lower()
while word not in synonyms.keys() and word not in synonyms.values():
    print('Такого слова в словаре нет.')
    word = input('Введите слово: ').lower()
if word in synonyms.keys():
    print('Синоним:', synonyms[word].title())
elif word in synonyms.values():
    for element in synonyms.keys():
        if word == synonyms[element]:
            print('Синоним:', element.title())