class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def is_feasible(target):
            k = 1
            last = position[0]
            for idx, num in enumerate(position[1:]):
                if num - last >= target:
                    k += 1
                    last = num
            if k >= m:
                return True
            return False
        
        l, r = 0, position[-1]
        while l < r:
            mid = (l+r+1)//2
            if is_feasible(mid):
                l = mid
            else:
                r = mid-1
        return l