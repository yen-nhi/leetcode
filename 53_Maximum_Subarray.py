from typing import List
import unittest
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        sum = 0
        for num in nums:
            if sum < 0:
                sum = num
            else: 
                sum += num
            if max_sum < sum:
                max_sum = sum
        return max_sum


class TestMaxSubArray(unittest.TestCase):
    def test_1(self) -> None:
        self.assertEqual(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)
        
    def test_2(self) -> None:
        self.assertEqual(Solution().maxSubArray([1]), 1)

    def test_3(self) -> None:
        self.assertEqual(Solution().maxSubArray([5,4,-1,7,8]), 23)
