class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def feasible(target):
            cnt = 0
            group = 0
            for day in bloomDay:
                if target >= day:
                    cnt += 1
                    if cnt == k:
                        group += 1
                        cnt = 0
                        if group == m:
                            return True
                else:
                    cnt = 0
            return False
        left, right = 1, max(bloomDay)
        while left <= right:
            mid = (left+right)//2
            if feasible(mid):
                right = mid-1
            else:
                left = mid+1
        return left if feasible(left) else -1
            