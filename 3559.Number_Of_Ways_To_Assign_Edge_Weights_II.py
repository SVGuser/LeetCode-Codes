class Solution:
    def assignEdgeWeights(self, edges, queries):
        import sys
        sys.setrecursionlimit(10**6)
        
        MOD = 10**9 + 7
        n = len(edges) + 1
        LOG = 17  # since 2^17 > 1e5
        
        # Step 1: Build adjacency list
        graph = [[] for _ in range(n+1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Initialize parent table and depth
        parent = [[-1]*(n+1) for _ in range(LOG)]
        depth = [0]*(n+1)
        
        # DFS to fill parent[0] and depth
        def dfs(u, p):
            parent[0][u] = p
            for v in graph[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    dfs(v, u)
        
        dfs(1, -1)
        
        # Step 3: Binary lifting preprocessing
        for k in range(1, LOG):
            for v in range(1, n+1):
                if parent[k-1][v] != -1:
                    parent[k][v] = parent[k-1][parent[k-1][v]]
        
        # Step 4: LCA function
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            # Lift u up
            for k in range(LOG-1, -1, -1):
                if parent[k][u] != -1 and depth[parent[k][u]] >= depth[v]:
                    u = parent[k][u]
            if u == v:
                return u
            # Lift both up
            for k in range(LOG-1, -1, -1):
                if parent[k][u] != -1 and parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]
        
        # Step 5: Answer queries
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
            else:
                a = lca(u, v)
                d = depth[u] + depth[v] - 2*depth[a]
                ans.append(pow(2, d-1, MOD))
        return ans
