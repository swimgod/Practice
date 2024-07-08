from unittest import TestCase

from src.MergeTwoSortedLinkedLists import MergeTwoSortedLinkedLists, ListNode


class TestIsomorphic(TestCase):
    def test_case1(self):
        input_list_node_1 = ListNode(1)
        input_list_node_2 = ListNode(2)
        input_list_node_3 = ListNode(4)

        input_list_node_1.next = input_list_node_2
        input_list_node_2.next = input_list_node_3

        input_list_node_4 = ListNode(1)
        input_list_node_5 = ListNode(3)
        input_list_node_6 = ListNode(4)

        input_list_node_4.next = input_list_node_5
        input_list_node_5.next = input_list_node_6

        output_list_node_1 = ListNode(1)
        output_list_node_2 = ListNode(1)
        output_list_node_3 = ListNode(2)
        output_list_node_4 = ListNode(3)
        output_list_node_5 = ListNode(4)
        output_list_node_6 = ListNode(4)

        output_list_node_1.next = output_list_node_2
        output_list_node_2.next = output_list_node_3
        output_list_node_3.next = output_list_node_4
        output_list_node_4.next = output_list_node_5
        output_list_node_5.next = output_list_node_6

        expected_list_values = []
        output_cur_node = output_list_node_1
        while output_cur_node:
            expected_list_values.append(output_cur_node.val)
            output_cur_node = output_cur_node.next

        actual = MergeTwoSortedLinkedLists.mergeTwoLists(input_list_node_1, input_list_node_4)

        actual_list_values = []
        actual_cur_node = actual
        while actual_cur_node:
            actual_list_values.append(actual_cur_node.val)
            actual_cur_node = actual_cur_node.next

        self.assertEqual(expected_list_values, actual_list_values)
