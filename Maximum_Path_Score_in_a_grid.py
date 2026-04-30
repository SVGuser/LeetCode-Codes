from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[i][j][c] = max score at (i,j) with cost c
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        
        # Starting cell
        start_cost = 0 if grid[0][0] == 0 else 1
        if start_cost <= k:
            dp[0][0][start_cost] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                for c in range(k + 1):
                    if dp[i][j][c] == -1:
                        continue
                    
                    # Move down
                    if i + 1 < m:
                        add_score = grid[i+1][j]
                        add_cost = 0 if add_score == 0 else 1
                        if c + add_cost <= k:
                            dp[i+1][j][c+add_cost] = max(
                                dp[i+1][j][c+add_cost],
                                dp[i][j][c] + add_score
                            )
                    
                    # Move right
                    if j + 1 < n:
                        add_score = grid[i][j+1]
                        add_cost = 0 if add_score == 0 else 1
                        if c + add_cost <= k:
                            dp[i][j+1][c+add_cost] = max(
                                dp[i][j+1][c+add_cost],
                                dp[i][j][c] + add_score
                            )
        
        return max(dp[m-1][n-1])
