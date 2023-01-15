# TODO здесь писать код
class Person:
    """
    Базовый класс, описывающий человека
    """

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def set_name(self):
        """
        Сеттер возвращает имя
        :return: __name
        :rtype str
        """
        return self.__name

    def set_surname(self):
        """
        Сеттер возвращает фамилию
        :return: __surname
        :rtype str
        """
        return self.__surname

    def set_age(self):
        """
        Сеттер возвращает возраст
        :return: __age
        :rtype str
        """
        return self.__age


class Employee(Person):
    """
    Класс работник. Родитель Person
    """
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def calculate_salary(self):
        """
        Расчет зарплаты
        """
        pass


class Manager(Employee):
    """
    Класс описывает и рассчитывает зарплату менеджера. Родитель Employee
    :arg __salary (int)
    """
    __salary = 13000

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def calculate_salary(self):
        """
        Рассчитываеет зарплату и выводит сообщение на жкран
        """
        print('{} {}: возраст - {}, зарплата - {}'.format(
            self.set_name(),
            self.set_surname(),
            self.set_age(),
            self.__salary))


class Agent(Employee):
    """
    Класс описывает и рассчитывает зарплату агента. Родитель Employee
    :arg sold (int)
    """
    def __init__(self, name, surname, age, sold):
        super().__init__(name, surname, age)
        self.sold = sold

    def calculate_salary(self):
        """
        Рассчитывает зарплату и выводит сообщение на экран
        :return:
        """
        salary = 50000 + self.sold * 0.05
        print('{} {}: возраст - {}, зарплата - {}'.format(
            self.set_name(),
            self.set_surname(),
            self.set_age(),
            salary))


class Worker(Employee):
    """
    Класс описывает и рассчитывает зарплату работника. Родитель Person
    :arg money_per_hour (int)
    """

    def __init__(self, name, surname, age, money_per_hour):
        super().__init__(name, surname, age)
        self.money_per_hour = money_per_hour

    def calculate_salary(self):
        """
        Рассчитывает зарплату и выводит сообщение на экран
        :return:
        """
        salary = 100 * self.money_per_hour
        print('{} {}: возраст - {}, зарплата - {}'.format(
            self.set_name(),
            self.set_surname(),
            self.set_age(),
            salary))


with open('people.txt', 'r', encoding='utf-8') as file:
    for element in file:
        element = element.split()
        if len(element) == 3:
            human = Manager(element[0], element[1], element[2])
            human.calculate_salary()
        elif len(element) == 4:
            human = Agent(element[0], element[1], element[2], int(element[3]))
            human.calculate_salary()
        else:
            human = Worker(element[0], element[1], element[2], int(element[3]))
            human.calculate_salary()