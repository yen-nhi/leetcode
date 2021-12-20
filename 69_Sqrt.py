import unittest

class Solution:
    def binary_search(self, l, r, x):
        if l == r:
            return l
        mid = (l + r) // 2
        if mid**2 == x or mid**2 < x <(mid+1)**2:
            return mid
        elif mid**2 > x:
            return self.binary_search(l, mid, x)
        else:
            return self.binary_search(mid + 1, r, x)
        
    def mySqrt(self, x: int) -> int:
        return self.binary_search(0, x, x) 


class TestMySqrt(unittest.TestCase):
    def test_1(self) -> None:
        self.assertEqual(Solution().mySqrt(9), 3)

    def test_2(self) -> None:
        self.assertEqual(Solution().mySqrt(1500), 38)

    def test_3(self) -> None:
        self.assertEqual(Solution().mySqrt(0), 0)

    def test_4(self) -> None:
        self.assertEqual(Solution().mySqrt(1), 1)

    def test_5(self) -> None:
        self.assertEqual(Solution().mySqrt(654321), 808)
