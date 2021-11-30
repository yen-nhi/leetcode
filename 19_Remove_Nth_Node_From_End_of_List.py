from typing import Optional 
import unittest

class LinkedNode():
    def __init__(self, val=0, next=None) -> None:
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
        if not isinstance(o, LinkedNode):
            return False
        return self.val == o.val and self.next == o.next


class Solution:
    def removeNthFromEnd(self, head: Optional[LinkedNode], n: int) -> Optional[LinkedNode]:
        #Find length of linked list
        size = 1
        node = head
        while node.next is not None:
            size += 1
            node = node.next
        #Find node need to be removed
        if n == size:
            new_head = head.next
            head.next = None
            return new_head
             
        node = head
        for i in range(size - n):
            back_node = node
            node = node.next
            front_node = node.next

        #Remove node
        back_node.next = front_node
        node = None
        return head
        
        


class testRemoveNthFromEnd(unittest.TestCase):
    def test_1(self) -> None:
        self.assertEqual(Solution()
            .removeNthFromEnd(
                LinkedNode(1, LinkedNode(2, LinkedNode(3, LinkedNode(4, LinkedNode(5))))), 2),
                LinkedNode(1, LinkedNode(2, LinkedNode(3, LinkedNode(5)))))

    def test_2(self) -> None:
        self.assertEqual(Solution()
            .removeNthFromEnd(
                LinkedNode(1, LinkedNode(2, LinkedNode(3, LinkedNode(4, LinkedNode(5))))), 1),
                LinkedNode(1, LinkedNode(2, LinkedNode(3, LinkedNode(4)))))

    def test_3(self) -> None:
        self.assertEqual(Solution()
            .removeNthFromEnd(
                LinkedNode(1, LinkedNode(2, LinkedNode(3, LinkedNode(4, LinkedNode(5))))), 5),
                LinkedNode(2, LinkedNode(3, LinkedNode(4, LinkedNode(5)))))