class Solution:
    def rotatedDigits(self, n: int) -> int:
        good_digits = {'2', '5', '6', '9'}
        invalid = {'3', '4', '7'}
        count = 0
        for num in range(1, n+1):
            s = str(num)
            if any(d in invalid for d in s):
                continue
            if any(d in good_digits for d in s):
                count += 1
        return count
