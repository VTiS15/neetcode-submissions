class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        carry = 0
        for i in range(n - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += 1
                carry = 0
                break

        if carry:
            digits = [carry] + digits
        
        return digits
        