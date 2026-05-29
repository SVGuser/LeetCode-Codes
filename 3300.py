class Solution:
    def minElement(self, nums):
        # Helper function to compute digit sum
        def digit_sum(x):
            return sum(int(d) for d in str(x))
        
        # Compute digit sum for each element and return minimum
        return min(digit_sum(num) for num in nums)
