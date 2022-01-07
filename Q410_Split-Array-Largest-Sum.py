class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def check_groups(target):
            groups = 1
            cur_sum = 0
            for num in nums:
                cur_sum += num
                if cur_sum > target:
                    cur_sum = num
                    groups += 1
            return groups <= m
        
        # binary search
        left, right = max(nums), sum(nums)
        ans = right
        while left <= right:
            mid = (left+right)//2

            if check_groups(mid):
                ans = mid
                right = mid-1
            else:
                left = mid + 1
        return ans