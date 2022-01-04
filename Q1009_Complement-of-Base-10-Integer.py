class Solution:
    def bitwiseComplement(self, n: int) -> int:
        num = 2
        while num-1 < n:
            num <<= 1
        return num-1-n