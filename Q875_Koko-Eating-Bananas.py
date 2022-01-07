class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_k_banana(target):
            groups = 0
            for pile in piles:
                groups += pile//target
                if pile%target:
                    groups += 1
                if groups > h:
                    return False
            return True
        left, right = 1, sum(piles)
        ans = right
        while left < right:
            mid = (left+right)//2
            if can_eat_k_banana(mid):
                right = mid
                ans = right
            else:
                left = mid+1
        return ans