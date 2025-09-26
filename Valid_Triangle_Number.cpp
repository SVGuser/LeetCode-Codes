//First Approach:
Sorting ensures that for any i < j < k, nums[i] <= nums[j] <= nums[k].

Fix the largest side nums[k], then use two pointers to find how many pairs (i, j) satisfy nums[i] + nums[j] > nums[k].

If the condition holds, all elements between i and j also form valid triangles with nums[k].

🧠 Time Complexity:
Sorting: 
𝑂
(
𝑛
log
⁡
𝑛
)

Two-pointer scan: 
𝑂
(
𝑛
2
)
 in worst case
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int n = nums.size(), count = 0;
        sort(nums.begin(), nums.end());

        for (int k = n - 1; k >= 2; --k) {
            int i = 0, j = k - 1;
            while (i < j) {
                if (nums[i] + nums[j] > nums[k]) {
                    count += j - i;
                    --j;
                } else {
                    ++i;
                }
            }
        }

        return count;
    }
};
//Second Approach 
🧠 Why This Is More Optimized
Binary Search (upper_bound) finds the first index where nums[k] >= nums[i] + nums[j], so all indices before that are valid third sides.

This avoids scanning the entire tail of the array and leverages the sorted nature of nums.

Time Complexity:

Sorting: 
𝑂
(
𝑛
log
⁡
𝑛
)

Nested loops: 
𝑂
(
𝑛
2
)

Binary search inside loop: 
𝑂
(
log
⁡
𝑛
)

Total: 
𝑂
(
𝑛
2
log
⁡
𝑛
)
  class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int n = nums.size(), count = 0;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < n - 2; ++i) {
            if (nums[i] == 0) continue; // Skip zero-length sides
            for (int j = i + 1; j < n - 1; ++j) {
                int sum = nums[i] + nums[j];
                // Find the first index k such that nums[k] >= sum
                int k = upper_bound(nums.begin() + j + 1, nums.end(), sum - 1) - nums.begin();
                count += k - j - 1;
            }
        }

        return count;
    }
};

  
