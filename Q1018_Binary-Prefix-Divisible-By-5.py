class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        bin_s = ""
        res = []
        for idx, num in enumerate(A):
            bin_s += str(num)
            sum_ = int(bin_s, 2)
            res += [sum_ % 5 == 0]
        return res