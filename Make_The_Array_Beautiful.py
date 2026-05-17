class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        stack = []
        for nums in arr:
            if stack and ((stack[-1] >= 0 and nums < 0) or (stack[-1] < 0 and nums >= 0)):
                stack.pop()
            else:
                stack.append(nums)
        return stack
