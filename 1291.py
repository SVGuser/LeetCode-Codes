class Solution(object):
    def sequentialDigits(self, low, high):
        res = []
        queue = [i for i in range(1, 10)]  # start with digits 1–9
        
        while queue:
            num = queue.pop(0)
            if low <= num <= high:
                res.append(num)
            last_digit = num % 10
            if last_digit < 9:  # can still append next digit
                next_num = num * 10 + (last_digit + 1)
                if next_num <= high:
                    queue.append(next_num)
        
        return res
