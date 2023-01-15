# TODO здесь писать код

password = input('Придумайте пароль: ')
password_size = len(password)
up_letter = 0
up_symbol = False
while True:
    for symbol in password:
        if symbol.isdigit():
            up_letter += 1
        if symbol.isupper():
            up_symbol = True
    if up_symbol and password_size >= 8 and up_letter >= 3:
        print('Пароль надежный')
        break
    else:
        print('Пароль ненадежный. Придумайте пароль: ', end='')
        up_letter = 0
        password = input()
