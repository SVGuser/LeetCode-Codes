class Solution {
public:
    int numSubmat(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        int count = 0;

        // Step 1: Preprocess each row to store consecutive 1s ending at (i,j)
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                dp[i][j] = (mat[i][j] == 0) ? 0 : (j == 0 ? 1 : dp[i][j - 1] + 1);

        // Step 2: For each cell, look upward and count valid submatrices
        for (int j = 0; j < n; ++j) {
            for (int i = 0; i < m; ++i) {
                int minWidth = dp[i][j];
                for (int k = i; k >= 0 && minWidth > 0; --k) {
                    minWidth = min(minWidth, dp[k][j]);
                    count += minWidth;
                }
            }
        }

        return count;
    }
};
