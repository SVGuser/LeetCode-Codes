class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Step 1: Convert number to string to iterate over digits
        digits = str(n)
        
        # Step 2: Concatenate non-zero digits into a new integer
        non_zero_digits = "".join([d for d in digits if d != '0'])
        concatenated_num = int(non_zero_digits) if non_zero_digits else 0
        
        # Step 3: Compute sum of digits of original number
        digit_sum = sum(int(d) for d in digits)
        
        # Step 4: Multiply concatenated number with digit sum
        return concatenated_num * digit_sum
