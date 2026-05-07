class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0]*n
        suf = [0]*n
        ans = [0]*n
        pref[0] = nums[0]
        for i in range(1, n):
            pref[i] = max(pref[i-1], nums[i])
        suf[-1] = nums[-1]
        
        for i in range(n-2, -1, -1):
            suf[i] = min(suf[i+1], nums[i])
        ans[-1] = pref[-1]
        for i in range(n-2, -1, -1):
            ans[i] = pref[i]
            if pref[i] > suf[i+1]:
                ans[i] = ans[i+1]
        return ans
