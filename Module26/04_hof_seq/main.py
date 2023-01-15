# TODO здесь писать код
from collections.abc import Iterator


def QHofstadter(start: list) -> Iterator[int]:
    """
    Класс описывает формирование Q последовательности Хофштадтера
    :param: start(list) передает список значений
    :return: возвращает следующее число последовательности
    """
    if start != [1, 1]:
        return
    else:
        duplicate = start[:]
        while 1:
            number = duplicate[-duplicate[-1]] + duplicate[-duplicate[-2]]
            duplicate.append(number)
            yield number


count = 0
start_values = [1, 1]
sequence = QHofstadter(start_values)
print(start_values[0], start_values[1], end=' ')
for element in sequence:
    if count == 20:
        break
    print(element, end=' ')
    count += 1