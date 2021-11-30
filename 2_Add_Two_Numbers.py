from logging import NOTSET
from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
   
    def __repr__(self) -> str:
        array = []
        node = self
        while node:
            array.append(node.val)
            node = node.next
        return array.__repr__()

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, ListNode):
            return False
        return self.val == o.val and self.next == o.next
            

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        m = 0
        node1 = l1
        node2 = l2
        res = ListNode()
        head = res
        while True:
            if node1 is None:
                val1 = 0
            else:
                val1 = node1.val
                node1 = node1.next

            if node2 is None:
                val2 = 0
            else:
                val2 = node2.val
                node2 = node2.next
            
            res.val = (val1 + val2 + m) % 10
            m = (val1 + val2 + m) // 10

            if node1 is None and node2 is None and m <= 0:
                return head

            res.next = ListNode()
            res = res.next

class TestAddTwoNumbers(unittest.TestCase):
    
    def test_1(self) -> None:
        self.assertEqual(
            Solution().addTwoNumbers(
                ListNode(2, ListNode(4, ListNode(3))),
                ListNode(5, ListNode(6, ListNode(4)))
            ), ListNode(7, ListNode(0, ListNode(8, None))))
    def test_2(self) -> None:
        self.assertEqual(
            Solution().addTwoNumbers(
                ListNode(),
                ListNode()
            ), ListNode())
    def test_3(self) -> None:
        self.assertEqual(
            Solution().addTwoNumbers(
                ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
                ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
            ), ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1)))))))))

