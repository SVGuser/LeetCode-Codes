from typing import List
from math import gcd

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        max_val = max(nums)
        
        # Step 1: frequency count
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1
        
        # Step 2: count multiples
        multiples = [0] * (max_val + 1)
        for d in range(1, max_val + 1):
            for m in range(d, max_val + 1, d):
                multiples[d] += freq[m]
        
        # Step 3: count pairs with gcd = d
        gcd_pairs = [0] * (max_val + 1)
        for d in range(max_val, 0, -1):
            cnt = multiples[d]
            gcd_pairs[d] = cnt * (cnt - 1) // 2
            for m in range(2 * d, max_val + 1, d):
                gcd_pairs[d] -= gcd_pairs[m]
        
        # Step 4: prefix sums over sorted gcd values
        prefix = []
        total = 0
        for d in range(1, max_val + 1):
            if gcd_pairs[d] > 0:
                total += gcd_pairs[d]
                prefix.append((total, d))
        
        # Answer queries
        ans = []
        for q in queries:
            # binary search for smallest prefix >= q+1
            lo, hi = 0, len(prefix) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if prefix[mid][0] > q:
                    hi = mid
                else:
                    lo = mid + 1
            ans.append(prefix[lo][1])
        
        return ans
