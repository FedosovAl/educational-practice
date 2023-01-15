# TODO здесь писать код
def sorted_data():
    try:
        if len(string) < 3:
            raise IndexError
        if not string[0].isalpha():
            raise NameError
        if not '@' and '.' in string[1]:
            raise SyntaxError
        if not 10 <= int(string[2]) <= 99:
            raise ValueError
        registrations_good.write(element + '\n')
    except IndexError:
        registrations_bad.write(element + '   НЕ присутствуют все три поля' + '\n')
    except NameError:
        registrations_bad.write(element + '   Поле "Имя"содержит НЕ только буквы' + '\n')
    except SyntaxError:
        registrations_bad.write(element + '   Поле "Имейл" НЕ содержит @ и/или .(точку)' + '\n')
    except ValueError:
        registrations_bad.write(element + '   Поле "Возраст" НЕ является числом от 10 до 99' + '\n')


with open('registrations.txt', 'r', encoding='utf-8') as text:
    for string in text:
        print(string, end='')
with open('registrations_good.log', 'w', encoding='utf-8') as registrations_good:
    with open('registrations_bad.log', 'w', encoding='utf-8') as registrations_bad:
        with open('registrations.txt', 'r', encoding='utf-8') as registrations:
            for element in registrations:
                element = element.rstrip()
                string = element.split()
                sorted_data()
with open('registrations_bad.log', 'r', encoding='utf-8') as registrations_bad:
    print('Содержимое файла registrations_bad.log:')
    for bad_string in registrations_bad:
        print(bad_string, end='')
with open('registrations_good.log', 'r', encoding='utf-8') as registrations_good:
    print('\n\nСодержимое файла registrations_good.log:')
    for good_string in registrations_good:
        print(good_string, end='')
