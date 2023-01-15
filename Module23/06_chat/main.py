# TODO здесь писать код
import datetime

while True:
    try:
        user_name = input('Введите иммя пользователя: ')
        print('Выбирите одно из действий (введите 1 или 2): \n1. Посмотреть текущий текст чата.\n2. Отправить сообщение.')
        command = int(input('Ответ: '))
        if command == 1:
            with open('chat_history.txt', 'r', encoding='utf-8') as chat_history:
                history = chat_history.read()
                if len(history) == 0:
                    print('В чате еще не было сообщений.')
                else:
                    print(history)
        elif command == 2:
            message = input('Введите сообщение: ')
            with open('chat_history.txt', 'a', encoding='utf-8') as message_to_chat:
                now = datetime.datetime.now()
                message_to_chat.write(str(now.strftime("%d-%m-%Y %H:%M")) + ' ' + user_name + ': ' + message + '\n')
                print('Сообщение отправлено!')
    except ValueError:
        print('Вы ввели некорректную команду. Попробуйте еще раз ')