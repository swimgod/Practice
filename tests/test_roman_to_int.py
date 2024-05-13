from unittest import TestCase

from src.RomanToIntSolution import RomanToIntSolution


class TestRomanToInt(TestCase):
    def test_case_1(self):
        expected = 3
        actual = RomanToIntSolution.romanToInt("III")
        self.assertEqual(expected, actual)

    def test_case_2(self):
        expected = 58
        actual = RomanToIntSolution.romanToInt("LVIII")
        self.assertEqual(expected, actual)

    def test_case_3(self):
        expected = 1994
        actual = RomanToIntSolution.romanToInt("MCMXCIV")
        self.assertEqual(expected, actual)

    def test_case_4(self):
        expected = 4
        actual = RomanToIntSolution.romanToInt("IV")
        self.assertEqual(expected, actual)

    def test_case_5(self):
        expected = 3
        actual = RomanToIntSolution.romanToInt2("III")
        self.assertEqual(expected, actual)

    def test_case_6(self):
        expected = 58
        actual = RomanToIntSolution.romanToInt2("LVIII")
        self.assertEqual(expected, actual)

    def test_case_7(self):
        expected = 1994
        actual = RomanToIntSolution.romanToInt2("MCMXCIV")
        self.assertEqual(expected, actual)

    def test_case_8(self):
        expected = 4
        actual = RomanToIntSolution.romanToInt2("IV")
        self.assertEqual(expected, actual)
