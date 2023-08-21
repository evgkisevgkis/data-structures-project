"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import *


class TestStack(unittest.TestCase):
    def test_stack(self):
        test1 = Stack
        self.assertTrue(test1)

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        data = stack.pop()
        self.assertTrue(data, 'data1')

    def test_pop_2(self):
        stack = Stack()
        stack.push('data1')
        stack.pop()
        self.assertIsNone(stack.top)

    def test_stack_str(self):
        stack = Stack()
        stack.push('data1')
        data = str(stack)
        self.assertTrue(data, 'data1')


if __name__ == '__main__':
    unittest.main()
