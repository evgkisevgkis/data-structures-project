class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        if self.head:
            new_node.next_node = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        if self.tail:
            self.tail.next_node = new_node
            self.tail = new_node
        else:
            self.tail = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ""
        while node:
            ll_string += f"{str(node.data)} -> "
            node = node.next_node

        ll_string += "None"
        return ll_string

    def to_list(self):
        """Вывод данных списка списком"""
        data_list = []
        cursor = self.head
        while cursor:
            data_list.append(cursor.data)
            cursor = cursor.next_node
        return data_list
