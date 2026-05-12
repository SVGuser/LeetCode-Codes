from typing import List
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        left, right = 0, sum(t[0] for t in tasks) + max(t[1] for t in tasks)
        ans = right
        def can_finish(energy: int) -> bool:
            for actual, minimum in tasks:
                if energy < minimum:
                    return False
                energy -= actual
            return True
        while left <= right:
            mid = (left + right) // 2
            if can_finish(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
