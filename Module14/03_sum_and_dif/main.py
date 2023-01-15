# TODO здесь писать код

def input_number_caclulate_and_input_summ(number):
    summ = 0
    while number !=0:
        digit = number % 10
        summ += digit
        number //= 10
    print('Сумма чисел:', summ)
    return summ

def input_number_caclulate_and_input_count_digits(number):
    count = 0
    while number !=0:
        number //= 10
        count += 1
    print('Количество цифр:', count)
    return count

entered_number = int(input('Введите число: '))
summ_of_numbers = input_number_caclulate_and_input_summ(entered_number)
count_of_digits = input_number_caclulate_and_input_count_digits(entered_number)
difference = summ_of_numbers - count_of_digits
print('Разность суммы и количества цифр:', difference)
