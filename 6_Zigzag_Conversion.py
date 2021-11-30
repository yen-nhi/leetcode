from typing import List
import unittest
import math

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        numColumns = max(math.ceil((len(s)-1)/(numRows-1)), 1)
        table = [ [''] * numColumns for i in range(numRows)]
        array = list(s)
        array.reverse()
        i, j = 0, 0
        
        for j in range(numColumns):
            if j == 0:
                range_i = range(numRows)
            elif j % 2 != 0:
                range_i = range(numRows - 2, -1, -1)
            else:
                range_i = range(1, numRows)
            for i in range_i:
                if array:
                    table[i][j] = array.pop()
                else:
                    break
        result = ''
        for row in table:
            joined = ''.join(row)
            result += joined
        return result       
        

class TestIsPalindrome(unittest.TestCase):
    def test_1(self) -> None:
        self.assertEqual(Solution().convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

    def test_2(self) -> None:
        self.assertEqual(Solution().convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")

    def test_3(self) -> None:
        self.assertEqual(Solution().convert("A", 2), "A")
