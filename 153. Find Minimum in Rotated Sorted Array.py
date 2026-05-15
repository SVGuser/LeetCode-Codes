from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, m = 0, len(nums) - 1
        while l < m:
            mid = (l + m) // 2
            if nums[mid] > nums[m]:
                l = mid + 1
            else:
                m = mid
        return nums[l]
