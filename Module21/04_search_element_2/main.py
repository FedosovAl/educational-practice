# TODO здесь писать код

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_value(struct, key):
    if key in struct:
        return struct[key]
    for element in struct.values():
        if isinstance(element, dict):
            result = find_value_by_depth(element, key)
            if result:
                break
    else:
        result = None
    return result


def find_value_by_depth(structure, desired_key, level=None):
    if level is None:
        result = find_value(structure, desired_key)
        return result
    else:
        if desired_key in structure:
            return structure[desired_key]
        if level > 1:
            for element in structure.values():
                if isinstance(element, dict):
                    result = find_value_by_depth(element, desired_key, level - 1)
                    if result:
                        break
            else:
                result = None
            return result


text = input('Введите искомый ключ: ')
question = input('Хотите ввести максимальную глубину? Y/N: ').upper()
if question == 'Y':
    maximum_depth = int(input('Введите максимальную глубину: '))
    value = find_value_by_depth(site, text, level=maximum_depth)
else:
    value = find_value_by_depth(site, text)
if value:
    print(value)
else:
    print('Такого ключа нет.')
