violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

# TODO здесь писать код

added_song = []
song = True
total_time = 0
number_of_songs = int(input('Сколько песен выбрать? '))
for count in range(number_of_songs):
    print('Название', count + 1, 'песни:', end=' ')
    song_name = input()
    for name in added_song:
        if name == song_name:
            print('Вы уже добавили эту песню. Выберите другую песню:', end=' ')
            song_name = input()
    for element in range(len(violator_songs)):
        if violator_songs[element][0] == song_name:
            song = True
            total_time += violator_songs[element][1]
            break
        else:
            song = False
        added_song.append(song_name)
    if not song:
        print('Такой песни нет.')
print('\nОбщее время звучания песен:', round(total_time, 2), 'минуты')

