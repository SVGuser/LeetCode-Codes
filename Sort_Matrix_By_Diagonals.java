class Solution {
    public int[][] sortMatrix(int[][] grid) {
        int n = grid.length;
        Map<Integer, List<Integer>> mp = new HashMap<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int diag = i - j;
                mp.computeIfAbsent(diag, k -> new ArrayList<>()).add(grid[i][j]);
            }
        }
…                int diag = i - j;
                List<Integer> list = mp.get(diag);
                grid[i][j] = list.remove(list.size() - 1); // take from back
            }
        }
        return grid;
    }
}
