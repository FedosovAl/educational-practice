# TODO здесь писать код

people_count = int(input('Кол-во человек: '))
counter = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', counter, 'человек.')
people = list(range(1, people_count + 1))
delete_position = 0
for _ in range(people_count - 1):
    print('Текущий круг людей', people)
    start_position = delete_position % len(people)
    print(start_position)
    delete_position = (start_position + counter - 1) % len(people)
    print(delete_position)
    print('Начало счёта с номера', people[start_position])
    print('Выбывает человек под номером', people[delete_position])
    people.remove(people[delete_position])
    print()
print('Остался человек под номером', people)
