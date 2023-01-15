# TODO здесь писать код
import random


class Karma:
    """
    Класс карма
    :arg current_karma (int) передается знаечение текущей кармы
    """
    __karma = 500

    def __init__(self, current_karma):
        self.current_karma = current_karma

    def get_current_karma(self):
        """
        Возвращает значение текущей кармы

        :return: current_karma
        :rtype int
        """
        return self.current_karma

    def achieve_enlightenment(self):
        """
        Возвращает значение достижения просветления

        :return: True: если текущее значение кармы больше или равно константе, иначе False
        :rtype bool
        """
        if self.current_karma >= self.__karma:
            return True
        else:
            return False

    def add_karma(self):
        """
        Прибавляет количество кармы к текущему значению

        :exception если выпало исключение, записывает его в файл karma.log
        """
        if random.randint(1, 10) == 1:
            with open('karma.log', 'a', encoding='utf-8') as file:
                exception = random.choice([
                    'KillError',
                    'DrunkError',
                    'CarCrashError',
                    'GluttonyError',
                    'DepressionError'])
                file.write(exception + '\n')
                print('Ой! Попалось исключение', exception)
        else:
            self.current_karma += random.randint(1, 7)


karma = Karma(0)
day = 1
while True:
    print('День {}. Текущая карма {}'.format(day, karma.get_current_karma()))
    karma.add_karma()
    if karma.achieve_enlightenment():
        print('День {}. Текущая карма {}'.format(day, karma.get_current_karma()))
        break
    day += 1
print('Вы достигли просветления за {} дней.'.format(day))