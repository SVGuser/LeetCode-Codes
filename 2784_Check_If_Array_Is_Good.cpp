#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isGood(vector<int>& nums) {
        int n = nums.size() - 1;
        unordered_map<int,int> freq;
        
        for (int x : nums) freq[x]++;
        
        // Check values 1 to n-1 appear exactly once
        for (int val = 1; val < n; val++) {
            if (freq[val] != 1) return false;
        }
        // Check n appears exactly twice
        return freq[n] == 2 && freq.size() == n;
    }
};
