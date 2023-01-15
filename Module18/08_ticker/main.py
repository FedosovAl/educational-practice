# TODO здесь писать код

first_string = input('Введите 1-ю строку: ')
second_string = input('Введите 2-ю строку: ')
first_symbols = []
after_permutation = []
second_symbols = []
first_symbols.extend(first_string)
second_symbols.extend(second_string)
shift_count = 0
if first_string == second_string:
    print('Строки равны.')
else:
    while shift_count < len(first_string):
        if len(first_string) == len(second_string):
            for element in range(len(first_string)):
                if first_symbols[element] == first_symbols[len(first_string) - 1]:
                    after_permutation.insert(0, first_symbols[len(first_string) - 1])
                else:
                    after_permutation.append(first_symbols[element])
            shift_count += 1
            if after_permutation == second_symbols:
                print(f'Первая строка получается из второй со сдвигом {shift_count}')
                break
            else:
                first_symbols = after_permutation
                after_permutation = []
        else:
            print('Количество символов в строках разное. Не получится поолучить 1-ю строку из 2-ой.')
            break
    else:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')

