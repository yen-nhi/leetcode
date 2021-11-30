from typing import List
import unittest

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dic = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_dic:
                return [nums_dic[target - nums[i]], i]
            if nums[i] not in nums_dic:
                nums_dic[nums[i]] = i
        

class TestTwoSum(unittest.TestCase):
    def test_1(self) -> None:
        self.assertEqual(
            sorted(Solution().twoSum([2,7,11,15], 9)), 
            [0, 1]
            )

    def test_2(self) -> None:
        self.assertEqual(
            sorted(Solution().twoSum([3,2,4], 6)), 
            [1, 2]
            )

    def test_3(self) -> None:
        self.assertEqual(
            sorted(Solution().twoSum([3,3], 6)), 
            [0, 1]
            )
