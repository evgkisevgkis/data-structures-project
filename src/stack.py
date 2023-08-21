class Node:
    """Класс для узла стека"""

    def __init__(self, data):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = None


class Stack:
    """Класс для стека"""
    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def __str__(self):
        return self.top.data

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        node = self.top
        if not node:
            return None
        self.top = node.next_node
        return node.data
