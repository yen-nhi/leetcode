from typing import List
import unittest

class Solution:
    def swap(self,arr, x, y):
        arr[x], arr[y] = arr[y], arr[x]
        return arr

    def permute(self, nums: List[int]) -> List[List[int]]:
        r = len(nums) - 1
        result = []
        arr = []
        def backtracking(l, r):
            if l == r: 
                result.append(nums)
            else:
                for i in range(r+1):
                    self.swap(nums, 0, i)
                    backtracking(l+1, r)
                    self.swap(nums, 0, i)
        return result
                    

print(Solution().permute([1,2,3]))  






class TestPermute(unittest.TestCase):
    def test_1(self) -> None:
        self.assertEqual(sorted(Solution().permute([1,2,3])), sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]))

    def test_2(self) -> None:
        self.assertEqual(sorted(Solution().permute([1,2,3])), sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]))

    def test_3(self) -> None:
        self.assertEqual(sorted(Solution().permute([1])), sorted([[1]]))