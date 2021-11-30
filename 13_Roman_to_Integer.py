import unittest
from unittest import result

class Solution:
    def romanToInt(self, s: str) -> int:
        value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        n = len(s)
        if n == 1:
            return value[s]
        for i in range(n-1):
            if value[s[i]] < value[s[i+1]]:
                result -= value[s[i]]
            else:
                result += value[s[i]]
        result += value[s[n-1]]
        return result


class testRomanToInt(unittest.TestCase):
    def test_1(self) -> None:
        self.assertEqual(Solution().romanToInt('III'), 3)

    def test_2(self) -> None:
        self.assertEqual(Solution().romanToInt('XVII'), 17)

    def test_3(self) -> None:
        self.assertEqual(Solution().romanToInt('LVIII'), 58)

    def test_4(self) -> None:
        self.assertEqual(Solution().romanToInt('C'), 100)