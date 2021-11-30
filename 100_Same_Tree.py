import unittest
from typing import Optional

class TreeNode():
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        array = []
        node = self
        for child in (node.left, node.right):
            while node:
                array.append(node.val)
                node = child
        return array.__repr__()

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, TreeNode):
            return False
        return self.val == o.val and self.left == o.left and self.right == o.right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False


class TestIsSameTree(unittest.TestCase):
    def test_1(self) -> None:
        self.assertTrue(Solution().isSameTree(
            TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4))),
            TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))
        ))

    def test_2(self) -> None:
        self.assertFalse(Solution().isSameTree(
            TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4))),
            TreeNode(1, TreeNode(3, TreeNode(4)), TreeNode(2))
        ))

    def test_3(self) -> None:
        self.assertTrue(Solution().isSameTree(
            None, None
            ))

