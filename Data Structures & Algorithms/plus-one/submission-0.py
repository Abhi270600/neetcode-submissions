class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1

        for i in range(len(digits) - 1, -1, -1):

            sum_val = digits[i] + carry

            digits[i] = sum_val % 10
            carry = sum_val // 10
        
        if carry:
            digits.insert(0, carry)
        
        return digits
