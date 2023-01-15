# TODO здесь писать код
import re

if __name__ == '__main__':
    numbers = ['9999999999', '999999-999', '99999x9999']
    for element in range(len(numbers)):
        if re.match(r'\b[8,9]{1}[0-9]{9}\b', numbers[element]):
            print(f'{element + 1}-й номер: всё в порядке')
        else:
            print(f'{element + 1}-й номер: не подходит')