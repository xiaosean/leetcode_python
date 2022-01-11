class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def bin_(s):
            n = len(s)
            i = 0
            sum_ = 0
            while i<n:
                if s[n-i-1]=="1":
                    sum_ += 1<<i
                i += 1
            return sum_
        return bin(bin_(a)+bin_(b))[2:]
            