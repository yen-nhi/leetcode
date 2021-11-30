from typing import List
import unittest
from unittest import result
from unittest.result import failfast

class Solution:  
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # node = 0
        # stack = [0]
        # arr = [[0]]
        # res = []
        # while stack:
        #     node = stack.pop()
        #     last_path = arr.pop()
        #     for v in graph[node]:
        #         stack.append(v)
        #         arr.append(last_path + [v]) 
        #     if node == len(graph)-1:
        #         res.append(last_path )
        # return res
        result = []
        path = []
        def findPaths(node):      
            path.append(node)
            if node == len(graph) - 1:
                result.append(path.copy())
            for v in graph[node]:
                findPaths(v)
            path.pop()
        
        findPaths(0)
        return result

print(Solution().allPathsSourceTarget([[1, 2], [3], [3], []]))
                
class TestAllPathsSourceTarget(unittest.TestCase):

    def test_1(self) -> None:
        self.assertEqual(sorted(Solution().allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]])), sorted([[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]))

    def test_2(self) -> None:
        self.assertEqual(sorted(Solution().allPathsSourceTarget([[4,3,1],[3,2,4],[],[4],[]])), sorted([[0,4],[0,3,4],[0,1,3,4],[0,1,4]]))

    def test_3(self) -> None:
        self.assertEqual(sorted(Solution().allPathsSourceTarget([[1,3],[2],[3],[]])), sorted([[0,1,2,3],[0,3]]))
