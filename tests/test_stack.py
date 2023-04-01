import unittest
from src import stack


class TestStack(unittest.TestCase):
    test_stack = stack.Stack()

    def test_push_to_stack(self):
        self.test_stack.push('test')
        self.assertEqual(self.test_stack, self.test_stack)

    def test_pop_from_stack(self):
        self.test_stack.push('data1')
        data = self.test_stack.pop()
        self.assertEqual(data, 'data1')
