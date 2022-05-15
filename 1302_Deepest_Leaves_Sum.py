from typing import Optional, List
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    deepest_leaves_sum = 0
    max_h = 0
    # def deepestLeavesSum(self, deepest_leaves:List):

    def deepestLeavesSum(self, root: Optional[TreeNode], h: int) -> int:
        if not root.left and not root.right:
            if h == self.max_h:
                self.deepest_leaves_sum += root.val
            elif h > self.max_h:
                self.deepest_leaves_sum = root.val
        if h > self.max_h:
            self.max_h += 1
        if root.left:
            self.deepestLeavesSum(root.left, h+1)
        if root.right:
            self.deepestLeavesSum(root.right, h+1)
        return self.deepest_leaves_sum
            
        

class TestDeepestLeavesSum(unittest.TestCase):

    def test_1(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        assert Solution().deepestLeavesSum(root, 0) == 5

    def test_2(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        assert Solution().deepestLeavesSum(root, 0) == 9

    def test_3(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4, None, TreeNode(6)), TreeNode(5)), TreeNode(3))
        assert Solution().deepestLeavesSum(root, 0) == 6
        
root = TreeNode(1, TreeNode(2, TreeNode(4, None, TreeNode(6)), TreeNode(5)), TreeNode(3))
print(Solution().deepestLeavesSum(root, 0))