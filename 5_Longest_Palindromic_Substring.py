import unittest

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        n = len(s)
        if n == 1:
            return s
        for i in range(n-1):
            j = 1
            while i-j >= 0 and i+j < n and s[i+j] == s[i-j]:
                j += 1
            if (j-1)*2 + 1 > len(longest):
                longest = s[i-j+1: i+j]

            if s[i] == s[i+1]:
                j = 1
                while i-j >= 0 and i+1+j < n and s[i-j] == s[i+1+j]:
                    j += 1
                if (j-1)*2 + 2 > len(longest):
                    longest = s[i-j+1: i+1+j]

        return longest



class testLongestPalindrome(unittest.TestCase):
    def test_1(self)-> None:
        self.assertEqual(Solution().longestPalindrome('aeabbbace'), 'abbba')

    def test_2(self)-> None:
        self.assertEqual(Solution().longestPalindrome('aeabbace'), 'abba')

    def test_3(self)-> None:
        self.assertEqual(Solution().longestPalindrome('abcdefghj'), 'a')

    def test_4(self)-> None:
        self.assertEqual(Solution().longestPalindrome('aa'), 'aa')

    def test_5(self)-> None:
        self.assertEqual(Solution().longestPalindrome('a'), 'a')


