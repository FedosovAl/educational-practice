# TODO здесь писать код
from typing import List
from functools import reduce

if __name__ == "__main__":
    floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
    names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
    numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
    new_floats = list(map(lambda element: round(element ** 3, 3), floats))
    print('Каждое число из списка floats в 3-ей степени:', new_floats)
    new_names = list(filter(
        lambda element: element is not None, map(lambda element: element if len(element) >= 5 else None, names)))
    print('Имена минимум из 5 букв из списка names:', new_names)
    new_numbers = reduce(lambda number, next_number: number * next_number, numbers)
    print('Произведение всех чисел в списке numbers:', new_numbers)
