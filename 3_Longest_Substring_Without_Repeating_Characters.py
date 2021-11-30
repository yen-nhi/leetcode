import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": 
            return 0
        dic = dict()
        i = 0
        longest = 0
        for j in range(len(s)):
            if s[j] in dic and dic[s[j]] >= i:
                if j - i > longest:
                    longest = j - i
                i = dic[s[j]] + 1
            dic[s[j]] = j
        return max(longest, len(s) - i)


class TestlengthOfLongestSubstring(unittest.TestCase):
    def test_4(self) -> None:
        self.assertEqual(Solution().lengthOfLongestSubstring("uwfhjtyuirfghbdcnjsuewyufjnkdiuhgfftfcguhjndksl"), 15)

    def test_4(self) -> None:
        self.assertEqual(Solution().lengthOfLongestSubstring(" abc d"), 5)

    def test_4(self) -> None:
        self.assertEqual(Solution().lengthOfLongestSubstring(""), 0)

    def test_4(self) -> None:
        self.assertEqual(Solution().lengthOfLongestSubstring(" "), 1)
   
