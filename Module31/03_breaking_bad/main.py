# TODO здесь писать код
import re
import json
import requests

if __name__ == '__main__':
    my_req = requests.get('https://www.breakingbadapi.com/api/deaths')
    data = json.loads(my_req.text)
    print(data)
    max_death = 0

