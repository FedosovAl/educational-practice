# TODO здесь писать код
def find_and_output_three_similar_digits():
    for number in range(start_year, stop_year + 1):
        first_digit = number // 1000
        second_digit = number // 100 % 10
        third_digit = number // 10 % 10
        fourth_digit = number % 10
        if first_digit == second_digit == third_digit or second_digit == third_digit == fourth_digit or first_digit == third_digit == fourth_digit or first_digit == second_digit == fourth_digit:
            print(number)

start_year = int(input('Введите первый год: '))
stop_year = int(input('Введите второй год: '))
while (start_year < 1000 or start_year > 9999) or (stop_year < 1000 or stop_year > 9999):
    print('Ошибка ввода! Год должен состоять из 4-х цифр.')
    start_year = int(input('Введите первый год: '))
    stop_year = int(input('Введите второй год: '))
print('Годы от ' + str(start_year) + ' до ' + str(stop_year) + ' с тремя одинаковыми цифрами:')
find_and_output_three_similar_digits()