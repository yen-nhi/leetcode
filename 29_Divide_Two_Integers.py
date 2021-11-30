import unittest

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend > 0 and divisor > 0:            
            result = dividend//divisor
        elif dividend <= 0 and divisor < 0:
            result = dividend//divisor
        else:
            result = -(-dividend//divisor)
        if result > 2**31 - 1:
            return result - 1
        return result

class testDivide(unittest.TestCase):
    def test_1(self) -> None:
        self.assertEqual(Solution().divide(-7, 3), -2)
    def test_2(self) -> None:
        self.assertEqual(Solution().divide(7, 3), 2)
    def test_3(self) -> None:
        self.assertEqual(Solution().divide(-2147483648, -1), 2147483647)
    def test_4(self) -> None:
        self.assertEqual(Solution().divide(-2147483648, -3), 715827882)