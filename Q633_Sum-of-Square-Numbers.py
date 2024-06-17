class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        seen = set()
        while i <= c:
            square_i = i**2
            seen.add(square_i)
            if c-square_i in seen:
                return True
            if square_i >= c:
                return False
            i += 1
        return False