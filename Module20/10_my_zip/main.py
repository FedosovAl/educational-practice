# TODO здесь писать код
def my_zip(symbols, number):
    return (
        (symbols[element], number[element])
        for element in range(min(len(symbols), len(number)))
    )


text = 'abcd'
numbers = (10, 20, 30, 40)
result = my_zip(text, numbers)
print(result)
for pairs in result:
    print(pairs)