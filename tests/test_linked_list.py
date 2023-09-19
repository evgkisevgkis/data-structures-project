"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_ll(self):
        test = LinkedList()
        test.insert_beginning(1)
        self.assertEqual(test.head.data, 1)

    def test_multiple(self):
        test = LinkedList()
        for n in range(5):
            test.insert_beginning(n)
        self.assertEqual(test.head.data, 4)


if __name__ == '__main__':
    unittest.main()
