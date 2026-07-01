class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
        
        # Step 2: Binary search on safeness factor
        def can_path(safe: int) -> bool:
            if dist[0][0] < safe: 
                return False
            visited = [[False]*n for _ in range(n)]
            dq = deque([(0,0)])
            visited[0][0] = True
            
            while dq:
                x, y = dq.popleft()
                if (x, y) == (n-1, n-1):
                    return True
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and dist[nx][ny] >= safe:
                        visited[nx][ny] = True
                        dq.append((nx, ny))
            return False
        
        lo, hi = 0, n*2  # upper bound on safeness
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_path(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans
