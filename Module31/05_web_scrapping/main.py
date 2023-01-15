# TODO здесь писать код
import re
import requests

if __name__ == '__main__':
    my_req = requests.get('http://www.columbia.edu/~fdc/sample.html')
    result = re.findall(r'[<][h][3].+', my_req.text)
    final_result = []
    for element in result:
        delete_on_the_left = re.sub(r'[<][h][3].+[>]\b', '', element)
        deleting_on_the_right = re.sub(r'[<][/][h][3][>]', '', delete_on_the_left)
        final_result.append(deleting_on_the_right)
    print('Результат:', final_result)
