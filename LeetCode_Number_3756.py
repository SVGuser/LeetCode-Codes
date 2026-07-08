from typing import List
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        m = len(s)
        val = [0] * (m + 1)      
        cnt = [0] * (m + 1)     
        sumPre = [0] * (m + 1)  
        pow10 = [1] * (m + 1)     
        for i in range(1, m + 1):
            d = int(s[i - 1])
            val[i] = val[i - 1]
            cnt[i] = cnt[i - 1]
            sumPre[i] = sumPre[i - 1] + d
            if d != 0:
                val[i] = (val[i] * 10 + d) % MOD
                cnt[i] += 1
            pow10[i] = (pow10[i - 1] * 10) % MOD
        ans = []
        for l, r in queries:
            k = cnt[r + 1] - cnt[l] 
            x = (val[r + 1] - val[l] * pow10[k]) % MOD
            sum_digits = sumPre[r + 1] - sumPre[l]
            ans.append((x * sum_digits) % MOD)
        return ans
