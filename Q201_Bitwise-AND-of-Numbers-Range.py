class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
#         Nice solution, inspired from https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/56729/Bit-operation-solution(JAVA)
        # if m != n, than must have one digit zero
        bin_n = bin(n)
        bin_n = list(bin_n[2:])
        idx = 0
        while m != n:
            m = m >> 1
            n = n >> 1
            bin_n[-(idx+1)] = 0
            idx += 1
        return int("".join(map(str, bin_n)), 2)
            