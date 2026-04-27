class Solution {
public:
    bool hasValidPath(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> dirs = {
            {}, 
            {0,-1,0,1},    // type 1: left, right
            {-1,0,1,0},    // type 2: up, down
            {0,-1,1,0},    // type 3: left, down
            {0,1,1,0},     // type 4: right, down
            {0,-1,-1,0},   // type 5: left, up
            {0,1,-1,0}     // type 6: right, up
        };
        
        auto valid = [&](int x, int y, int dx, int dy) {
            if (x < 0 || y < 0 || x >= m || y >= n) return false;
            int t = grid[x][y];
            for (int k = 0; k < dirs[t].size(); k += 2) {
                if (dirs[t][k] == -dx && dirs[t][k+1] == -dy) return true;
            }
            return false;
        };
        // Breadth First Search
        queue<pair<int,int>> q;
        vector<vector<bool>> vis(m, vector<bool>(n,false));
        q.push({0,0});
        vis[0][0] = true;
        
        while (!q.empty()) {
            auto [x,y] = q.front(); q.pop();
            if (x == m-1 && y == n-1) return true;
            int t = grid[x][y];
            for (int k = 0; k < dirs[t].size(); k += 2) {
                int dx = dirs[t][k], dy = dirs[t][k+1];
                int nx = x+dx, ny = y+dy;
                if (valid(nx,ny,dx,dy) && !vis[nx][ny]) {
                    vis[nx][ny] = true;
                    q.push({nx,ny});
                }
            }
        }
        return false;
    }
};
