class Solution(object):
    def minScore(self, n, roads):
        parent = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

        # Merge all roads
        for u, v, w in roads:
            union(u, v)

        # Get the root of city 1
        root1 = find(1)

        # Find the smallest edge weight in the same group
        min_score = float('inf')
        for u, v, w in roads:
            if find(u) == root1 or find(v) == root1:
                min_score = min(min_score, w)

        return min_score
