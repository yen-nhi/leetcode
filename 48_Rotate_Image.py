from typing import List
import unittest
import math

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(math.ceil(n/2)):
            for j in range(n//2):
                (u, v) = (i, j)
                temp = matrix[i][j]
                for k in range(3):
                    matrix[u][v] = matrix[n-1-v][u]
                    (u, v) = (n-1-v, u)
                matrix[u][v] = temp
                

        
class TestRotate(unittest.TestCase):
    def test_1(self) -> None:
        image = [[1,2,3],[4,5,6],[7,8,9]]
        Solution().rotate(image)
        self.assertEqual(image, [[7,4,1],[8,5,2],[9,6,3]])

    def test_2(self) -> None:
        image = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        Solution().rotate(image)
        self.assertEqual(image, [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])  

    def test_3(self) -> None:
        image = [[1]]
        Solution().rotate(image)
        self.assertEqual(image, [[1]])      