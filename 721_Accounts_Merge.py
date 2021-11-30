from typing import List, NamedTuple
import unittest
from unittest import result

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dic = {}
        name_dic = {}
        n = 0
        #Transform input in to graph
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                if accounts[i][j] not in dic:
                    dic[accounts[i][j]] = n
                    name_dic[accounts[i][j]] = accounts[i][0]
                    n += 1
        graph = [[] for i in range(n)]
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])-1):
                graph[dic[accounts[i][j]]].append(dic[accounts[i][j+1]])
                graph[dic[accounts[i][j+1]]].append(dic[accounts[i][j]])
        print(dic)
        print(graph)
        #Find connected components of graph
        visited = [False for i in range(n)]
        components = []
        def DFS(v, arr):
            arr.append(v)
            visited[v] = True
            for u in graph[v]:
                if not visited[u]:
                    DFS(u, arr)
                
        for v in range(n):
            if not visited[v]:
                arr = []
                DFS(v, arr)
                components.append(arr)
        print(components)
        #Transform nodes from int to string
        dic = dict((v,k) for k,v in dic.items())
        result = []
        for group in components:
            group = [name_dic[dic[group[0]]]] + sorted(list(map(lambda item: dic[item], group)))
            result.append(group)
        return result

# print(Solution().accountsMerge(
#             [["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]]))
class TestAccountsMerge(unittest.TestCase):
    def test_1(self) -> None:
        self.assertEqual(sorted(Solution().accountsMerge(
            [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
        )), sorted([["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))

    def test_2(self) -> None:
        self.assertEqual(sorted(Solution().accountsMerge(
            [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
        )), sorted([["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]))

    def test_3(self) -> None:
        self.assertEqual(sorted(Solution().accountsMerge(
            [["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]]
        )), sorted([["David","David0@m.co","David1@m.co","David3@m.co","David4@m.co","David5@m.co"]]))
