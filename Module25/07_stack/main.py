# TODO здесь писать код
class Stack:
    """
    Класс описывает стек
    attributes: stack (list) список значений
    """
    def __init__(self):
        self.stack = []

    def __str__(self):
        return '; '.join(self.stack)

    def add_to_stack(self, element):
        """
        Добавляет элементы в стек
        :param element: передает значение
        """
        self.stack.append(element)

    def remove_from_stack(self):
        """
        Удаляет элементы из стека
        :return: None, если стек пуст или stack.pop(), значения в стеке есть
        """
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()


class TaskManager:
    """
    Класс описывает Менеджер задач

    attributes:
    tasks (dict) - словарь для записи значений
    new_tasks (dict) - словарь, перезаписывающий отсортированные значения словаря tasks

    """
    def __init__(self):
        self.tasks = dict()
        self.new_tasks = dict()

    def __str__(self):
        result = []
        for element in self.new_tasks.keys():
            result.append('{} {}\n'.format(element, self.new_tasks[element]))
        return ''.join(result)

    def sorted_tasks(self):
        """
        Сортирует значения и записывает в новый словарь
        """
        for element in sorted(self.tasks.keys()):
            self.new_tasks[element] = self.tasks[element]

    def new_task(self, task, priority):
        """
        Добавляет значения в словарь
        :param task (str): передает задачу для добавления в словарь
        :param priority (int): передает приоритет задачи для добавления в словарь
        """
        priority = str(priority)
        if priority not in self.tasks:
            self.tasks[priority] = Stack()
        self.tasks[priority].add_to_stack(task)

    def delete_task(self, my_task):
        """
        Удаляет элементы из словаря. Удаление происходит на основе стека.
        Удаление происходит до момента, пока не удален элемент, переданный из основного кода
        :param my_task (str): передает задачу для ее удаления
        """
        new_tasks = self.new_tasks
        for priority, tasks in new_tasks.items():
            tasks = str(tasks).split('; ')
            if len(tasks) > 1:
                for element in tasks[::-1]:
                    if element == my_task:
                        self.tasks[priority].remove_from_stack()
                        break
                    else:
                        self.new_tasks[priority].remove_from_stack()
                break
            self.new_tasks[priority].remove_from_stack()


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
manager.sorted_tasks()
print(manager)
manager.delete_task("сдать дз")
print(manager)