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
    def insert(self, node, head) -> None:
        prev_node = None
        list_node = head
        while list_node is not None:
            if list_node.val >= node.val:
                if prev_node is not None:
                    prev_node.next = node
                else:
                    head = node
                node.next = list_node
                return head
            prev_node = list_node
            list_node = list_node.next
        prev_node.next = node
        return head

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_of_sorted_list = None
        while head is not None:
            node = head
            head = head.next
            node.next = None
            if head_of_sorted_list is None:
                head_of_sorted_list = node
            else:
                head_of_sorted_list = self.insert(node, head_of_sorted_list)
        return head_of_sorted_list
            

class TestInsertionSortList(unittest.TestCase):
    def test_1(self) -> None:
        self.assertEqual(
            Solution().insertionSortList(ListNode(5, ListNode(9, ListNode(4, ListNode(7, ListNode(3)))))), 
            ListNode(3, ListNode(4, ListNode(5, ListNode(7, ListNode(9)))))
        )
    def test_2(self) -> None:
        self.assertEqual(
            Solution().insertionSortList(ListNode(1, ListNode(3, ListNode(8, ListNode(2, ListNode(10)))))), 
            ListNode(1, ListNode(2, ListNode(3, ListNode(8, ListNode(10)))))
        )

    def test_3(self) -> None:
        self.assertEqual(
            Solution().insertionSortList(ListNode(1)), 
            ListNode(1)
        )