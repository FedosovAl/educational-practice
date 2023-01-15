# TODO здесь писать код

text = input('Введите строку: ')
positions = [position for position in range(len(text)) if text[position] == 'h']
print(positions)
start = positions[0]
end = positions[len(positions) - 1] - 1
print(end)
print('Развернутая последовательность между первым и последним h:', text[end:start:-1])
