from unittest import TestCase, main
from stacks import MaxStack


class TestMaxStack(TestCase):
    def setUp(self):
        self.stack = MaxStack()
        self.stack.push(6)
        self.stack.push(2)
        self.stack.push(9)

    def test_push_pop(self):
        self.stack.push(7)
        self.assertEqual(self.stack.pop(), 7)

    def test_get_max(self):
        self.assertEqual(self.stack.pop(), 9)
        self.assertEqual(self.stack.get_max(), 6)


if __name__ == '__main__':
    main()
