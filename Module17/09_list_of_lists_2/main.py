nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# TODO здесь писать код
numbers = [number for first_numbers in nice_list
           for second_numbers in first_numbers
           for number in second_numbers]
print(numbers)
