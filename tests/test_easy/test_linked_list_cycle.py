from unittest import TestCase

from src.easy.LinkedListCycle import LinkedListCycle, ListNode


class TestLinkedListCycle(TestCase):
    def test_case1(self):
        node_1 = ListNode(3)
        node_2 = ListNode(2)
        node_3 = ListNode(0)
        node_4 = ListNode(-4)

        node_1.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_2

        head = [3, 2, 0, -4]

        expected = True
        actual = LinkedListCycle.hasCycle(node_1)
        self.assertEqual(expected, actual)
