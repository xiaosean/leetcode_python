class Solution:
    def reverseBits(self, n: int) -> int:
        bin_ = bin(n)[2:]
        bin_ = '0'*(32-len(bin_)) + bin_
        res = int(str(bin_)[::-1], 2)
        return res