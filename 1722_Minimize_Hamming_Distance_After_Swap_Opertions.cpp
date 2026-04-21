#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumHammingDistance(vector<int>& source, vector<int>& target, vector<vector<int>>& allowedSwaps) {
        int n = source.size();
        vector<vector<int>> adj(n);
        
        // Build adjacency list from allowed swaps
        for (auto &edge : allowedSwaps) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        
        vector<bool> visited(n, false);
        int ans = 0;
        
        // DFS to find connected components
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                vector<int> compSrc, compTgt;
                stack<int> st;
                st.push(i);
                visited[i] = true;
                
                while (!st.empty()) {
                    int node = st.top(); st.pop();
                    compSrc.push_back(source[node]);
                    compTgt.push_back(target[node]);
                    
                    for (int nei : adj[node]) {
                        if (!visited[nei]) {
                            visited[nei] = true;
                            st.push(nei);
                        }
                    }
                }
                
                // Compare frequency counts of source vs target in this component
                unordered_map<int,int> freq;
                for (int val : compSrc) freq[val]++;
                for (int val : compTgt) {
                    if (freq[val] > 0) freq[val]--;
                    else ans++;
                }
            }
        }
        return ans;
    }
};
