from typing import List, Optional


class JumpGame:
    @staticmethod
    def canJump(nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1

        return True

    @staticmethod
    def canJumpFailure(nums: List[int]) -> bool:
        class TreeNode:
            def __init__(self, val=0, nodes=None):
                self.val = val
                if nodes is None:
                    self.nodes = []

        initial_node = TreeNode()
        initial_node.nodes = [TreeNode(0+i) for i in range(1, nums[0] + 1)]

        if len(nums) == 1:
            return True

        def generate_nodes(nodes):
            last_index = len(nums) - 1
            for node in nodes:
                if node.val < len(nums):
                    max_node_count = nums[node.val] + 1
                    node.nodes = [TreeNode(node.val + i) for i in range(1, max_node_count) if node.val + i <= last_index]
                    generate_nodes(node.nodes)

        def traverse_tree_node(nodes: List[TreeNode], temp_list: List):
            for node in nodes:
                temp_list.append(node.val)
                traverse_tree_node(node.nodes, temp_list)

        generate_nodes(initial_node.nodes)
        temp = []
        traverse_tree_node(initial_node.nodes, temp)
        return (len(nums) - 1) in temp
