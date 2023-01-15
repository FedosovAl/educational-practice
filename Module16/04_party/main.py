guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

# TODO здесь писать код

print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
answer = input('Гость пришёл или ушёл? ')
answer = answer.lower()
guest = False
while answer != 'пора спать':
    guest_name = input('Имя гостя: ')
    if answer == 'пришёл' or answer == 'пришел':
        if len(guests) < 6:
            guests.append(guest_name)
            print('Привет, ' + guest_name + '!')
        else:
            print('Прости', guest_name,'но мест нет.')
    elif answer == 'ушёл' or answer == 'ушел':
        for name in guests:
            if name == guest_name:
                guest = True
                break
            else:
                guest = False
        if guest:
            guests.append(guest_name)
            print('Пока, ' + guest_name + '!')
        else:
            print('Такого гостя нет.')
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
    answer = input('Гость пришёл или ушёл? ')
    answer = answer.lower()
print('\nВечеринка закончилась, все легли спать.')