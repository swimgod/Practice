from unittest import TestCase

from src.easy.MaxDepthBinaryTree import MaxDepthBinaryTree, TreeNode


class TestMaxDepthBinaryTree(TestCase):
    def test_case1(self):
        node_2 = TreeNode(9)
        node_3 = TreeNode(15)
        node_4 = TreeNode(7)
        node_5 = TreeNode(20, left=node_3, right=node_4)
        tree_node = TreeNode(val=3, left=node_2, right=node_5)

        expected = 3
        actual = MaxDepthBinaryTree.maxDepth(tree_node)
        self.assertEqual(expected, actual)
