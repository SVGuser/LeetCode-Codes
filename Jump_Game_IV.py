from collections import deque, defaultdict

class Solution(object):
    def minJumps(self, arr):
        n = len(arr)
        if n <= 1:
            return 0
        
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
        
        queue = deque([(0, 0)])   # (index, steps)
        visited = set([0])
        
        while queue:
            i, steps = queue.popleft()
            if i == n - 1:
                return steps
            
            # neighbors: i-1, i+1, and all indices with same value
            neighbors = graph[arr[i]]
            if i + 1 < n:
                neighbors.append(i + 1)
            if i - 1 >= 0:
                neighbors.append(i - 1)
            
            for nei in neighbors:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, steps + 1))
            
            # clear to avoid revisiting same-value indices again
            graph[arr[i]] = []
        
        return -1
