class Date:
    """ Класс описывает дату"""
    @classmethod
    def separate(cls, date_recording: str) -> tuple[int, int, int]:
        """
        Разбивает строку на день, месяц и год
        :param: date_recording(str) - передает дату
        :return:
            day(int) - возвращает день
            month(int) - возвращает месяц
            year(int) - возвращает год
        """
        string = date_recording.split('-')
        day = int(string[0])
        month = int(string[1])
        year = int(string[2])
        return day, month, year

    @classmethod
    def is_date_valid(cls, date_recording: str) -> bool:
        """
        Проверяет дату на корректность.
        Если день больше 0 и меньше 32, месяц больше 0 и меньше 13, год больше 0,
        то возвращает True. Иначе возвращает False.
        :param: date_recording(str) - передает дату
        :return:
            True(bool) - дата корректна
            False(bool) - дата некорректна
        """
        day, month, year = cls.separate(date_recording)
        if(0 < day < 32) and (0 < month < 13) and year > 0:
            return True
        else:
            return False

    @classmethod
    def from_string(cls, date_recording: str) -> str:
        """
        Конвертирует строку отдельно в день, месяц и год
        :param: date_recording(str) - передает дату
        :return: возвращает строку, разбитую отдельно на день, месяц и год
        """
        day, month, year = cls.separate(date_recording)
        return f'День: {day}   месяц: {month}   год: {year}'


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))