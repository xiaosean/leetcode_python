class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_ = nums[0]
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] > nums[-1]:
                lo = mid+1
            else:
                hi = mid
        return nums[lo]
                