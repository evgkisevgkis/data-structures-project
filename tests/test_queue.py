"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import *


class TestQueue(unittest.TestCase):
    def test_queue(self):
        test = Queue()
        self.assertTrue(test)

    def test_str(self):
        test = Queue()
        self.assertEqual(str(test), "")

    def test_enqueue(self):
        test = Queue()
        test.enqueue(24)
        test.enqueue(25)
        self.assertEqual(test.dequeue(), 24)


if __name__ == '__main__':
    unittest.main()
