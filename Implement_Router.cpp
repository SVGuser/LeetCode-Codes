#include <queue>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

class Router {
    int memoryLimit;
    queue<tuple<int,int,int>> q;
    set<tuple<int,int,int>> s;
    map<int,vector<int>> m;

public:
    Router(int memoryLimit) : memoryLimit(memoryLimit) {}

    bool addPacket(int src, int dst, int time) {
        auto p = tuple(src,dst,time);
        if (s.count(p)) return false;
        if (q.size() == memoryLimit) {
            auto old = q.front(); q.pop(); s.erase(old);
            auto& v = m[get<1>(old)];
            v.erase(lower_bound(v.begin(), v.end(), get<2>(old)));
        }
        q.push(p); s.insert(p); m[dst].push_back(time);
        return true;
    }

    vector<int> forwardPacket() {
        if (q.empty()) return {};
        auto p = q.front(); q.pop(); s.erase(p);
        auto& v = m[get<1>(p)];
        v.erase(lower_bound(v.begin(), v.end(), get<2>(p)));
        return {get<0>(p), get<1>(p), get<2>(p)};
    }

    int getCount(int dst, int st, int et) {
        auto& v = m[dst];
        return upper_bound(v.begin(), v.end(), et) - lower_bound(v.begin(), v.end(), st);
    }
};
