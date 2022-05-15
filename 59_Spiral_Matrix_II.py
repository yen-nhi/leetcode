import unittest
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for i in range(n)]
        i, j, num = 0, -1, 0
        while num < n*n:
            while j < n-1 and matrix[i][j+1] == 0:
                num += 1
                j += 1
                matrix[i][j] = num
            while i < n-1 and matrix[i+1][j] == 0:
                num += 1
                i += 1
                matrix[i][j] = num
            while j > 0 and matrix[i][j-1] == 0:
                num += 1
                j -= 1
                matrix[i][j] = num
            while i > 0 and matrix[i-1][j] == 0:
                num += 1
                i -= 1
                matrix[i][j] = num
        return matrix


print(Solution().generateMatrix(5))    