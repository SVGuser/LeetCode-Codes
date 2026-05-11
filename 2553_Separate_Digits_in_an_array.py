class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            u = []
            while x:
                u.append(x%10)
                x //= 10
            ans.extend(u[::-1])
        return ans