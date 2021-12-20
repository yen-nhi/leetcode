from typing import List
import unittest

class Solution:
    def dfs_height(self, node, graph, visited):
        visited[node] = True
        child_h = -1
        for child in graph[node]:
            if not visited[child]:
                child_h = max(child_h, self.dfs_height(child, graph, visited))
        return child_h + 1


    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #build the graph list
        graph = [[] for i in range(n)]
        for (u, v) in edges:
            graph[u].append(v)
            graph[v].append(u)

        #calculate height for each node as root
        mht = []
        min_h = n
        for v in range(n):
            visited = [False] * n
            h = self.dfs_height(v, graph, visited)
            if h < min_h:
                mht = [v]
                min_h = h
            elif h == min_h:
                mht.append(v)
        return mht


class TestFindMinHeightTrees(unittest.TestCase):
    def test_1(self) -> None:
        self.assertEqual(
            sorted(Solution().findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])),
            [3,4]
        )

    def test_2(self) -> None:
        self.assertEqual(
            sorted(Solution().findMinHeightTrees(1, [])),
            [0]
        )

    def test_3(self) -> None:
        self.assertEqual(
            sorted(Solution().findMinHeightTrees(4, [[1,0],[1,2],[1,3]])),
            [1]
        )