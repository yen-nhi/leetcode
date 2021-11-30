from typing import List
import unittest

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l != r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid
        if target > nums[l]:
            return l + 1
        return l


class TestSearchInsert(unittest.TestCase):
    def test_1(self) -> None:
        self.assertEqual(Solution().searchInsert([1,3,5,6], 5), 2)

    def test_2(self) -> None:
        self.assertEqual(Solution().searchInsert([1,3,5,6], 2), 1)

    def test_3(self) -> None:
        self.assertEqual(Solution().searchInsert([1,3,5,6], 7), 4)

    def test_4(self) -> None:
        self.assertEqual(Solution().searchInsert([1,3,5,6], 0), 0)

