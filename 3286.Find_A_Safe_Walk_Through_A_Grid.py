from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        # dist[i][j] will store the minimum health cost to reach cell (i, j)
        dist = [[float('inf')] * n for _ in range(m)]
        
        # Initialize the starting cell
        dist[0][0] = grid[0][0]
        
        # 0-1 BFS queue storing (row, col)
        q = deque([(0, 0)])
        
        # 4-directional moves
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check grid boundaries
                if 0 <= nr < m and 0 <= nc < n:
                    # Cost to move to the next cell is the value of that cell (0 or 1)
                    new_cost = dist[r][c] + grid[nr][nc]
                    
                    # If we found a path with a smaller health cost, update and push to queue
                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        
                        # 0-1 BFS optimization: 
                        # Cells with 0 cost go to the front, 1 cost go to the back
                        if grid[nr][nc] == 0:
                            q.appendleft((nr, nc))
                        else:
                            q.append((nr, nc))
                            
        # If the minimum cost to reach the end is less than our health, 
        # we finish with at least 1 health point remaining.
        return dist[m - 1][n - 1] < health
