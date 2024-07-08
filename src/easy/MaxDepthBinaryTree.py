from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaxDepthBinaryTree:
    @staticmethod
    def maxDepth(root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = MaxDepthBinaryTree.maxDepth(root.left)
        right = MaxDepthBinaryTree.maxDepth(root.right)
        return 1 + max(left, right)
