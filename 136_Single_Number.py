from typing import List
import unittest

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        nums.sort()
        for i in range(0, n, 2):
            if i == n-1:
                return nums[i]
            if nums[i] != nums[i+1]:
                return nums[i]


class TestSingleNumber(unittest.TestCase):
    def test_1(self) -> None:
        self.assertEqual(Solution().singleNumber([4,1,2,1,2]), 4)

    def test_2(self) -> None:
        self.assertEqual(Solution().singleNumber([1]), 1)

    def test_3(self) -> None:
        self.assertEqual(Solution().singleNumber([1,2,3,4,5,5,3,2,1]), 4)
