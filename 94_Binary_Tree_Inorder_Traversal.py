from typing import Optional, List
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array = []
        def traversal(node):
            if node is not None:
                traversal(node.left)
                array.append(node.val)
                traversal(node.right)            
        traversal(root)
        return array

class TestInorderTraversal(unittest.TestCase):
    def test_1(self) -> None:
        tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        self.assertEqual(Solution().inorderTraversal(tree), [1, 3, 2])

    def test_2(self) -> None:
        tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5))
        self.assertEqual(Solution().inorderTraversal(tree), [3, 2, 4, 1, 5])

    def test_3(self) -> None:
        tree = TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(4, TreeNode(5))))
        self.assertEqual(Solution().inorderTraversal(tree), [1, 3, 2, 5, 4])