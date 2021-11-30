from typing import List
import unittest

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        current_dic = {}
        n = len(words)
        result = []
        for letter in words[0]:
            current_dic[letter] = current_dic.get(letter, 0) + 1
        for word in words[1:]:
            n_dic = {}
            for letter in word:
                n_dic[letter] = n_dic.get(letter, 0) + 1
            for key in current_dic.keys():
                if key not in n_dic:
                    current_dic[key] = 0
                else:
                    current_dic[key] = min(current_dic[key], n_dic[key])
        for key in current_dic.keys():
            for i in range(current_dic[key]):
                result.append(key)
        return result    

class TestCommonChars(unittest.TestCase):
    def test_1(self) -> None:
        self.assertEqual(
            sorted(Solution().commonChars(["bella","label","roller"])),
            ["e","l","l"]
            )

    def test_2(self) -> None:
        self.assertEqual(
            sorted(Solution().commonChars(["cool","lock","cook"])),
            ["c","o"]
            )

    def test_3(self) -> None:
        self.assertEqual(
            sorted(Solution().commonChars(["lllo", "o"])),
            ["o"]
            )


