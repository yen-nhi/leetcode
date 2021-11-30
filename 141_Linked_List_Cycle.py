from typing import Optional
import unittest

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        pos = dict()
        while node:
            if node not in pos:
                pos[node] = True
            else:
                return True
            node = node.next
        return False

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

class testHasCycle(unittest.TestCase):
    def test_1(self) -> None:
        self.assertTrue(Solution().hasCycle(node1))
    def test_2(self) -> None:
        self.assertFalse(Solution().hasCycle(ListNode(1)))