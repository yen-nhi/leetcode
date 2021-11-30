from typing import List
import unittest

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)
        for i in range(n//2):
            if s[i] != s[-1-i]:
                return False
        return True


class TestIsPalindrome(unittest.TestCase):
    def test_1(self) -> None:
        self.assertTrue(Solution().isPalindrome(11111111**2))

    def test_2(self) -> None:
        self.assertTrue(Solution().isPalindrome(126547105501745621))

    def test_3(self) -> None:
        self.assertFalse(Solution().isPalindrome(126547105521745621))

    def test_4(self) -> None:
        self.assertFalse(Solution().isPalindrome(-121))


