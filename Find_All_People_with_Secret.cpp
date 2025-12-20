class Solution {
public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        sort(meetings.begin(), meetings.end(), [](auto &a, auto &b){return a[2]<b[2];});
        vector<int> knows(n,0);
        knows[0]=knows[firstPerson]=1;
        int i=0;
        while(i<meetings.size()){
            int t=meetings[i][2];
            unordered_map<int,vector<int>> g;
            unordered_set<int> s;
            int j=i;
            while(j<meetings.size() && meetings[j][2]==t){
                int x=meetings[j][0],y=meetings[j][1];
                g[x].push_back(y);
                g[y].push_back(x);
                if(knows[x]) s.insert(x);
                if(knows[y]) s.insert(y);
                j++;
            }
            queue<int> q;
            for(int p:s) q.push(p);
            unordered_set<int> vis;
            while(!q.empty()){
                int u=q.front();q.pop();
                if(vis.count(u)) continue;
                vis.insert(u);
                knows[u]=1;
                for(int v:g[u]) if(!vis.count(v)) q.push(v);
            }
            i=j;
        }
        vector<int> ans;
        for(int k=0;k<n;k++) if(knows[k]) ans.push_back(k);
        return ans;
    }
};
