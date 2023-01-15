def calculating_math_func(data, number):
    if number in factorials.keys():
        result = factorials[number]
    else:
        result = 1
        for index in range(1, number + 1):
            result *= index
        data[number] = result
    result /= number ** 3
    result = result ** 10
    return result


# TODO оптимизировать функцию

factorials = {}
print(calculating_math_func(factorials, 5))
print(calculating_math_func(factorials, 5))
