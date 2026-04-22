from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def withinTwoEdits(a: str, b: str) -> bool:
            diff = 0
            for x, y in zip(a, b):
                if x != y:
                    diff += 1
                    if diff > 2:
                        return False
            return True
        
        ans = []
        for q in queries:
            for d in dictionary:
                if withinTwoEdits(q, d):
                    ans.append(q)
                    break
        return ans
