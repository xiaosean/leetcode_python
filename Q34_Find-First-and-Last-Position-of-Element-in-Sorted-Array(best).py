class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (hi+lo)//2
            if nums[mid] < target:
                lo = mid+1
            else:
                hi = mid
        if lo >= len(nums) or nums[lo] != target:
            return res
        res[0] = lo
        # Because we already found the index of target, so we can start from lo
        lo, hi = lo, len(nums)-1
        while lo < hi:
            mid = (hi+lo)//2+1
            if nums[mid] > target:
                hi = mid-1
            else:
                lo = mid
        res[1] = hi
        return res