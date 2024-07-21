class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l < r:
            mid = (l+r+1)//2
            val = mid * mid
            if val == x:
                return mid
            elif val < x:
                l = mid
            else:
                r = mid-1
        return int(l)
