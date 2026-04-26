class Solution {
public:
    bool containsCycle(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> visited(m, vector<int>(n, 0));
        
        function<bool(int,int,int,int,char)> dfs = [&](int x, int y, int px, int py, char ch) {
            if (visited[x][y]) return true;
            visited[x][y] = 1;
            
            int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
            for (auto &d : dirs) {
                int nx = x + d[0], ny = y + d[1];
                if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
                if (grid[nx][ny] != ch) continue;
                if (nx == px && ny == py) continue; // skip parent
                
                if (dfs(nx, ny, x, y, ch)) return true;
            }
            return false;
        };
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    if (dfs(i, j, -1, -1, grid[i][j])) return true;
                }
            }
        }
        return false;
    }
};
