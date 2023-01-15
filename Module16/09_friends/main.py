# TODO здесь писать код

friends = int(input('Количество друзей: '))
debt_document = int(input('Долговых расписок: '))
friend_number = []
friends_list = []
for count in range(friends):
    friend_number.append(count +1)
    friend_number.append(0)
    friends_list.append(friend_number)
    friend_number = []
for number in range(debt_document):
    print()
    print(str(number + 1) + '-я' + ' расписка:')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    while to_whom == from_whom:
        print('Человек не может занимать сам себе. Введите данные еще раз:')
        to_whom = int(input('Кому: '))
        from_whom = int(input('От кого: '))
    debt = int(input('Сколько: '))
    friends_list[to_whom - 1][1] -= debt
    friends_list[from_whom - 1][1] += debt
print('\nБаланс друзей:')
result = ''
for count in friends_list:
    for element in count:
        if result == '':
            print(str(element) + ':', end=' ')
        else:
            print(str(element))
    print()