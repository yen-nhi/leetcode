from typing import List
import unittest

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j:
            if min(height[i], height[j]) * (j - i) > max_area:
                max_area = min(height[i], height[j]) * (j - i)
            if height[i] < height[j]:
                i += 1
            else: 
                j -= 1
        return max_area  

class TestCommonChars(unittest.TestCase):
    def test_1(self) -> None:
        self.assertEqual(Solution().maxArea([1,8,6,2,5,4,8,3,7]), 49)

    def test_2(self) -> None:
        self.assertEqual(Solution().maxArea([4,3,2,1,4]), 16)

    def test_3(self) -> None:
        self.assertEqual(Solution().maxArea([2,3,4,5,18,17,6]), 17)
