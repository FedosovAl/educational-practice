# TODO здесь писать код
from collections.abc import Iterator
from typing import Any, Optional


class Node:
    """
    Класс описывает узел: значение и ссылку на следующий элемент
    :arg:
    value(any) передает значение
    next(Node) передает ссылку на следующий элемент
    """
    def __init__(self, value: Optional[Any] = None, next: Optional['Node'] = None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return '{}'.format(str(self.value))


class LinkedList:
    """
    Класс описывает односвязный список
    """
    def __init__(self):
        self.head: Optional[Node] = None
        self.length = 0

    def __str__(self) -> str:
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return '[{}]'.format(' '.join(values))

    def __iter__(self) -> Optional[Any]:
        item = self.head
        while item is not None:
            yield item
            item = item.next

    def append(self, elem: Any) -> None:
        """
        Добавляет элемент в конец списка.
        Если головной элемент списка пустой, то переданное значение становится головным элементом.
        Иначе перебирает значения списка, пока следющий элемент не будет равен None и вставляет переданное значение.
        :param: elem(any)
        """
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
            return
        end = self.head
        while end.next:
            end = end.next
        end.next = new_node
        self.length += 1

    def get(self, index: int) -> Optional[Any]:
        """
        Получает и возвращает значение по индексу
        :param: index(int) передает индекс искомого значения
        Если длина списка равна 0 или длина списка меньше переданного индекса, то вызывается исключение.
        Если в списке есть значения, то проходим по списку, пока не будет найден переданный индекс.
        :return: current_node(any) возвращает найденное значение
        """
        current_node = self.head
        current_index = 0
        previous = None
        if self.length == 0 or self.length < index:
            raise IndexError
        while current_node is not None:
            if current_index == index:
                return current_node
            previous = current_node
            current_node = current_node.next
            current_index += 1
        previous.next = current_node.next

    def remove(self, index) -> None:
        """
        Удаляет элемент из списка
        :param: index(int) передает индекс для удаление элемента
        Если длина списка равна 0 или длина списка меньше переданного индекса, то вызывается исключение.
        Если значения в списке есть, проходим по списку, пока не будет найден переданный индекс.
        Если индекс текущего элемента равен переданному индексу, ссылка предыдущего элемента на
        текущий элемент прерывается и теперь предыдущий элемент ссылается на следующий элемент.
        """
        current_node = self.head
        current_index = 0
        previous = None
        if self.length == 0 or self.length < index:
            raise IndexError
        if current_node is not None:
            if index == 0:
                self.head = current_node.next
                self.length -= 1
                return
            while current_node is not None:
                if current_index == index:
                    break
                previous = current_node
                current_node = current_node.next
                current_index += 1
            previous.next = current_node.next
            self.length -= 1


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Полученный список: ', my_list)
my_list.remove(1)
print('Список после удаления 2-го элемента:', my_list)
print('Элемент с индексом 0:', my_list.get(0))
for element in my_list:
    print(element, end=' ')