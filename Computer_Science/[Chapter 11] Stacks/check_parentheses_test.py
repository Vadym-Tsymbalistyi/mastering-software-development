from unittest import TestCase, main
from stacks import check_parentheses


class TestCheckParentheses(TestCase):
    def test_balanced_parentheses(self):
        self.assertTrue(check_parentheses('()'))
        self.assertTrue(check_parentheses('{}'))
        self.assertTrue(check_parentheses('({})'))

    def test_not_balanced_parentheses(self):
        self.assertFalse(check_parentheses('('))
        self.assertFalse(check_parentheses('){'))
        self.assertFalse(check_parentheses('})'))
        self.assertFalse(check_parentheses('))}'))


if __name__ == '__main__':
    main()
