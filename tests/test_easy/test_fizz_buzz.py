from unittest import TestCase

from src.easy.FizzBuzz import FizzBuzz


class TestFizzBuzz(TestCase):
    def test_case1(self):
        n = 3
        expected = ["1","2","Fizz"]
        actual = FizzBuzz.fizzBuzz2(n)
        self.assertEqual(expected, actual)
