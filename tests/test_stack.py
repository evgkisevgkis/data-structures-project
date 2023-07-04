"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import *


class TestStack(unittest.TestCase):
    def test_stack(self):
        test1 = Stack
        self.assertTrue(test1)


if __name__ == '__main__':
    unittest.main()
