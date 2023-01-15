# TODO здесь писать код
def sort_keys(frequencies_sort, elem):
    identical_values = {}
    keys = []
    result = {}
    for sym in frequencies_sort.keys():
        if frequencies[sym] == elem:
            identical_values[sym] = elem
    keys = sorted(identical_values.keys())
    for sym in keys:
        result[sym] = elem
    return result


alphabet = 'abcdefghijklmnopqrstuvwxyz'
file = open('text.txt', 'r')
text = file.read()
frequencies = {}
sorted_frequencies = {}
letters_count = 0
sorted_values = []
values_without_repetition = set()
result_keys = {}
final_result = {}
print('Содержимое файла text.txt:')
for element in text:
    print(element, end='')
    if element.isalpha():
        letters_count += 1
text = text.lower()
for symbol in text:
    if symbol.isalpha():
        number = text.count(symbol)
        part = round((number / letters_count), 3)
        frequencies[symbol] = part
sorted_values = sorted(frequencies.values())
sorted_values.reverse()
for element in sorted_values:
    for key in frequencies:
        if frequencies[key] == element:
            values_without_repetition.add(element)
            sorted_frequencies[key] = element
for element in values_without_repetition:
    result_keys = sort_keys(sorted_frequencies, element)
    final_result.update(result_keys)
file.close()
new_file = open('analysis.txt', 'w')
for key, value in final_result.items():
    record = key + ' ' + str(value) + '\n'
    new_file.write(record)
new_file.close()
new_file = open('analysis.txt', 'r')
new_text = new_file.read()
print('\n\nСодержимое файла analysis.txt:')
print(new_text)
new_file.close()