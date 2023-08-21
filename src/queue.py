class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None, prev_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if not self.head:
            new_node = Node(data)
            self.head = new_node
        elif not self.tail:
            new_node = Node(data)
            self.tail = new_node
            self.head.next_node = new_node
        else:
            new_node = Node(data)
            self.tail = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.head:
            return self.head.data
        else:
            return ""
