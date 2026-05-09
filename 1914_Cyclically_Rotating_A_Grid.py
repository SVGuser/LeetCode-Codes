from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2
        for layer in range(layers):
            elems = []
            for j in range(layer, n-layer):
                elems.append(grid[layer][j])
            for i in range(layer+1, m-layer-1):
                elems.append(grid[i][n-layer-1])
            for j in range(n-layer-1, layer-1, -1):
                elems.append(grid[m-layer-1][j])
            for i in range(m-layer-2, layer, -1):
                elems.append(grid[i][layer])
            L = len(elems)
            k_mod = k % L
            rotated = elems[k_mod:] + elems[:k_mod]
            idx = 0
            for j in range(layer, n-layer):
                grid[layer][j] = rotated[idx]; idx += 1
            for i in range(layer+1, m-layer-1):
                grid[i][n-layer-1] = rotated[idx]; idx += 1
            for j in range(n-layer-1, layer-1, -1):
                grid[m-layer-1][j] = rotated[idx]; idx += 1
            for i in range(m-layer-2, layer, -1):
                grid[i][layer] = rotated[idx]; idx += 1
        return grid
