#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int n = strs.size(), m = strs[0].size();
        vector<int> dp(m,1);
        int ans=1;
        for(int i=0;i<m;i++){
            for(int j=0;j<i;j++){
                bool ok=true;
                for(int k=0;k<n;k++){
                    if(strs[k][j]>strs[k][i]){
                        ok=false;
                        break;
                    }
                }
                if(ok) dp[i]=max(dp[i],dp[j]+1);
            }
            ans=max(ans,dp[i]);
        }
        return m-ans;
    }
};

int main(){
    vector<string> strs={"babca","bbazb"};
    Solution ob;
    cout<<ob.minDeletionSize(strs);
    return 0;
}
