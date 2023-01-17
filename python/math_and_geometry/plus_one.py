from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] += 1
        if digits[-1] > 9:
            digits[-1] = digits[-1] % 10
            carry = 1
        for i in range(len(digits)-2,-1,-1):
            digits[i] += carry
            carry = 0
            if digits[i] > 9:
                digits[i] = digits[i] % 10
                carry = 1
        if carry == 1:
            digits.insert(0,carry)
        return digits

if __name__ == "__main__":
    sol = Solution()
    sol.plusOne([9,9])