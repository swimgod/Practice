from unittest import TestCase

from src.medium.GasStation import GasStation


class TestGasStation(TestCase):
    def test_case1(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        expected = 3
        actual = GasStation.canCompleteCircuit(gas, cost)
        self.assertEqual(expected, actual)

    def test_case2(self):
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        expected = -1
        actual = GasStation.canCompleteCircuit(gas, cost)
        self.assertEqual(expected, actual)

    def test_case3(self):
        gas = [5,1,2,3,4]
        cost = [4,4,1,5,1]
        expected = 4
        actual = GasStation.canCompleteCircuit(gas, cost)
        self.assertEqual(expected, actual)

    def test_case4(self):
        gas = [0, 0, 0, 0, 0, 0, 2]
        cost = [0, 0, 0, 0, 0, 1, 0]
        expected = 6
        actual = GasStation.canCompleteCircuit(gas, cost)
        self.assertEqual(expected, actual)