site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

# TODO здесь писать код


def website_builder(website, product, title='title', h2 = 'h2'):
    if title in website:
        website[title] = 'Куплю/продам {} недорого'.format(product)
    if h2 in website:
        website[h2] = 'У нас самая низкая цена на {}'.format(product)
    for element in website.values():
        if isinstance(element, dict):
            website_builder(element, product, title)
    return website


def input_website(structure, depth=0):
    for key, value in structure.items():
        print('\t' * depth, key)
        if isinstance(value, dict):
            input_website(value, depth + 1)
        else:
            print('\t' * (depth + 1), value)


number_of_sites = int(input('Сколько будет сайтов? '))
for _ in range(number_of_sites):
    name = input('Введите название продукта для нового сайта: ')
    result = website_builder(site, name)
    input_website(result)