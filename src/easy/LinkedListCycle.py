from typing import List, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedListCycle:
    @staticmethod
    def hasCycle(head: Optional[ListNode]) -> bool:
        all_nodes = set()
        cur_node = head
        while cur_node and cur_node.next:
            all_nodes.add(cur_node)
            cur_node = cur_node.next
            if cur_node in all_nodes:
                return True
        return False
