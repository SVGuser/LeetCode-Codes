class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        // Sort in descending order to prioritize largest sides first
        sort(nums.begin(), nums.end(), greater<int>());

        // Check every triplet for triangle validity
        for (int i = 0; i < nums.size() - 2; ++i) {
            int a = nums[i], b = nums[i+1], c = nums[i+2];
            // Triangle inequality: sum of smaller two sides > largest side
            if (b + c > a) {
                return a + b + c;
            }
        }

        // No valid triangle found
        return 0;
    }
};
