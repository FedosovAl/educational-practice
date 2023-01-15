# TODO здесь писать код

import zipfile

archive = zipfile.ZipFile('voyna-i-mir.zip', 'r')
archive.extractall()
file = open('voyna-i-mir.txt', 'r', encoding='utf-8')
text = file.read()
letters_count = 0
frequencies = {}
sorted_values = []
sorted_frequencies = {}
for element in text:
    if element.isalpha():
        letters_count += 1
for symbol in text:
    if symbol.isalpha():
        number = text.count(symbol)
        part = round((number / letters_count), 6)
        frequencies[symbol] = part
print(frequencies)
sorted_values = sorted(frequencies.values())
sorted_values.reverse()
for element in sorted_values:
    for key in frequencies:
        if frequencies[key] == element:
            sorted_frequencies[key] = element
file.close()
new_file = open('result.txt', 'w')
for key, value in sorted_frequencies.items():
    record = key + ' ' + str(value) + '\n'
    new_file.write(record)
new_file.close()
new_file = open('result.txt', 'r')
new_text = new_file.read()
print('\n\nСодержимое файла analysis.txt:')
print(new_text)
new_file.close()