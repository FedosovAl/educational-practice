# TODO здесь писать код

def find_number_by_number_position(num_pos, nums, pos):
    while len(nums) - 1 != num_pos:
        nums.append(nums[pos] + (nums[pos + 1]))
        pos += 1
    return nums[num_pos - 1]


number_position = int(input('Введите позицию числа в ряде Фибоначчи: '))
numbers = [1, 1]
position = 0
result = find_number_by_number_position(number_position, numbers, position)
print('Число: ', result)
