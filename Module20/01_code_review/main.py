students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)

# TODO исправить код

def find_interests_and_length_of_surnames(data):
    all_interests = set()
    surnames = ''
    for number, student_data in data.items():
        for information, name in student_data.items():
            if information == 'interests':
                all_interests.update(name)
            if information == 'surname':
                surnames += name
    count_symbols = len(surnames)
    return all_interests, count_symbols


pairs = ()
pairs_list = []
for index, person in students.items():
    for key, value in person.items():
        if key == 'age':
            pairs = index, value
            pairs_list.append(pairs)
interests, length_surnames = find_interests_and_length_of_surnames(students)
print('Список пар "ID студента — возраст":', pairs_list)
print('Полный список интересов всех студентов:', interests)
print('Общая длина всех фамилий студентов:', length_surnames)