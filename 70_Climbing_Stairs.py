import unittest

class Solution:
    def climbStairs(self, n: int) -> int:
        #DP
        # the number of paths to reach  n steps is sum of 
        # (the number of paths to reach n-2 steps and the number of paths to reach n-1 steps)
        if n < 3:
            return n
        prev2, prev1 = 1, 2
        for i in range(3, n):
            temp = prev1 + prev2 
            prev2 = prev1
            prev1 = temp
        return prev1 + prev2
        


class TestClimbStairs(unittest.TestCase):
    def test_1(self) -> None:
        self.assertEqual(Solution().climbStairs(5), 8)

    def test_2(self) -> None:
        self.assertEqual(Solution().climbStairs(2), 2)

    def test_3(self) -> None:
        self.assertEqual(Solution().climbStairs(10), 89)