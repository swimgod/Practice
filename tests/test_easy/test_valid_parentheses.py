from unittest import TestCase

from src.easy.ValidParentheses import ValidParentheses


class TestValidParentheses(TestCase):
    def test_case1(self):
        s = "()"
        expected = True
        actual = ValidParentheses.isValid(s)
        self.assertEqual(expected, actual)

    def test_case2(self):
        s = "()[]{}"
        expected = True
        actual = ValidParentheses.isValid(s)
        self.assertEqual(expected, actual)

    def test_case3(self):
        s = "(]"
        expected = False
        actual = ValidParentheses.isValid(s)
        self.assertEqual(expected, actual)

    def test_case4(self):
        s = "{[]}"
        expected = True
        actual = ValidParentheses.isValid(s)
        self.assertEqual(expected, actual)

    def test_case5(self):
        s = "([)]"
        expected = False
        actual = ValidParentheses.isValid(s)
        self.assertEqual(expected, actual)

    def test_case6(self):
        s = "(("
        expected = False
        actual = ValidParentheses.isValid(s)
        self.assertEqual(expected, actual)