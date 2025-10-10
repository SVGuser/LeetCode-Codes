#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maximumEnergy(vector<int>& energy, int k) {
        int n = energy.size();
        vector<int> dp(n);

        // Fill dp from the back
        for (int i = n - 1; i >= 0; --i) {
            dp[i] = energy[i];
            if (i + k < n) {
                dp[i] += dp[i + k];
            }
        }

        // Return the maximum energy possible from any starting index
        return *max_element(dp.begin(), dp.end());
    }
};

int main() {
    // Example input
    vector<int> energy = {5, 2, -10, -5, 1};
    int k = 3;

    // Create an instance of Solution
    Solution sol;
    int result = sol.maximumEnergy(energy, k);

    // Output the result
    cout << "Maximum energy collected: " << result << endl;

    return 0;
}
