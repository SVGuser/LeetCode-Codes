class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        cnt = 0
        for i in range(num1, num2 + 1):
            s = str(i)
            n = len(s)
            for j in range(1, n-1):
                if (s[j] > s[j-1] and s[j] > s[j+1]) or \
                   (s[j] < s[j-1] and s[j] < s[j+1]):
                    cnt += 1
        return cnt
