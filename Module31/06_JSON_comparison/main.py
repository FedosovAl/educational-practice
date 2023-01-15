# TODO здесь писать код
import json

if __name__ == '__main__':
    def find_value_in_file(element: str, file: dict) -> str:
        """
        Рекурсивная функция для поиска значения по переданному ключу
        :param:
            element(str) - передает значение из diff_list
            file(dict) - передает словарь
        :return: value(str), current_result(str) - возвращает найденное значение

        """
        for name, value in file.items():
            if name == element:
                return value
            elif isinstance(value, dict):
                current_result = find_value_in_file(element, value)
                if current_result is not None:
                    return current_result
            elif isinstance(value, list):
                for item in value:
                    current_result = find_value_in_file(element, item)
                    if current_result is not None:
                        return current_result


    diff_list = ['services', 'staff', 'datetime']
    data = dict()
    with open('json_old.json', 'r', encoding='utf-8') as json_old:
        old_data = json.load(json_old)
        print('Данные, загруженные из json_old.json:', old_data)
    with open('json_new.json', 'r', encoding='utf-8') as json_new:
        new_data = json.load(json_new)
        print('Данные, загруженные из json_new.json:', new_data)
    result = []
    for diff_value in diff_list:
        old_value = find_value_in_file(diff_value, old_data)
        new_value = find_value_in_file(diff_value, new_data)
        if old_value == new_value:
            continue
        else:
            data[diff_value] = new_value
            result.append(data)
            data = dict()
    print('Различия:', result)
    with open('result.json', 'w') as new_file:
        json.dump(result, new_file, indent=4)
