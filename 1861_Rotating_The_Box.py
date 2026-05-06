from typing import List

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        
        # Step 1: Apply gravity row by row
        for row in boxGrid:
            empty = n - 1
            for j in range(n - 1, -1, -1):
                if row[j] == '*':
                    empty = j - 1
                elif row[j] == '#':
                    row[j], row[empty] = row[empty], row[j]
                    empty -= 1
        
        # Step 2: Rotate 90° clockwise
        rotated = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m - 1 - i] = boxGrid[i][j]
        
        return rotated
