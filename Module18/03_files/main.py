# TODO здесь писать код

way = input('Введите путь: ').lower()
start = ('@', '№', '$', '%', '^', '&', '*', '()')
end = ('.txt', '.docx.')
if way.startswith(start):
    print('Ошибка: название начинается на один из специальных символов.')
elif not way.endswith(end):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Путь указан верно.')