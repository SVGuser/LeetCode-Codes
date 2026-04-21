from typing import List
from collections import defaultdict

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        adj = defaultdict(list)
        for u, v in allowedSwaps:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        ans = 0

        for i in range(n):
            if not visited[i]:
                stack = [i]
                visited[i] = True
                compSrc, compTgt = [], []

                while stack:
                    u = stack.pop()
                    compSrc.append(source[u])
                    compTgt.append(target[u])
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            stack.append(v)

                freq = defaultdict(int)
                for x in compSrc: freq[x] += 1
                for y in compTgt:
                    if freq[y] > 0: freq[y] -= 1
                    else: ans += 1

        return ans
