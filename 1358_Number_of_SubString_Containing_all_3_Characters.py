class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = [0] * 3
        res = 0
        left = 0
        for ryt in range(n):
            cnt[ord(s[ryt]) - ord('a')] += 1
            while all(cnt):
                res += n - ryt
                cnt[ord(s[left]) - ord('a')] -= 1
                left += 1
        return res
