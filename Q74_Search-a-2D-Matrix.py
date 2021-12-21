class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        size = m*n
        def reshape(num):
            return num//n, num%n
        
        lo, hi = 0, size
        while lo < hi:
            mid = (lo+hi)//2
            y, x = reshape(mid)
            num = matrix[y][x]
            if num == target:
                return True
            elif num < target:
                lo = mid+1
            else:
                hi = mid