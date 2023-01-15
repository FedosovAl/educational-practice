# TODO здесь писать код

number = int(input('Введите число: '))
minimum_divisor = 99999999
for digit in range(2, number + 1):
    if number % digit == 0 and digit < minimum_divisor:
        minimum_divisor = digit
print('Наименьший делитель, отличный от единицы:', minimum_divisor)