from collections import Counter
from typing import List
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        if 1 in cnt:
            ans = cnt[1] if cnt[1] % 2 == 1 else cnt[1] - 1
            del cnt[1]
        for x in list(cnt.keys()):
            length = 0
            val = x
            while cnt.get(val, 0) > 1:
                length += 2
                val *= val
            if cnt.get(val, 0) == 1:
                length += 1
            ans = max(ans, length)
        return ans
