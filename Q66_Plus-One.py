class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        plus_ = 1
        for i in range(n-1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                plus_ = 0
                break
        if plus_:
            digits = [1] + digits
        return digits