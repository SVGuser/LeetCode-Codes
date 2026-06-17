class Solution(object):
    def processStr(self, s, k):
        length = 0
        for ch in s:
            if ch.isalpha():
                length += 1
            elif ch == '*':
                if length > 0:
                    length -= 1
            elif ch == '#':
                length *= 2
            elif ch == '%':
                pass
        if k >= length:
            return '.'

        for ch in reversed(s):
            if ch.isalpha():
                if k == length - 1:
                    return ch
                length -= 1
            elif ch == '*':
                length += 1
            elif ch == '#':
                if k >= length // 2:
                    k -= length // 2
                length //= 2
            elif ch == '%':
                k = length - 1 - k
        return '.'
