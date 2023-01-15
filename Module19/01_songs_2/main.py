violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

# TODO здесь писать код

result = 0
answer = int(input('Сколько песен выбрать? '))
for number in range(1, answer + 1):
    name_song = input(f'Введите название {number} песни: ')
    if name_song not in violator_songs.keys():
        print('Ошибка ввода, такой песни нет.')
    result += violator_songs[name_song]
print('\nОбщее время звучания песен:', round(result, 2))
