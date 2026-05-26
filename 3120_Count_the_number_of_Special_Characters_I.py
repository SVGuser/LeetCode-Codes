class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Create sets for lowercase and uppercase letters
        lower_set = set()
        upper_set = set()
        
        # Fill sets
        for ch in word:
            if ch.islower():
                lower_set.add(ch)
            elif ch.isupper():
                upper_set.add(ch)
        
        # Count characters that exist in both sets
        count = 0
        for ch in lower_set:
            if ch.upper() in upper_set:
                count += 1
        
        return count
