class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # dfs solution to solve this problem
        nums = [-float('inf')] + nums + [-float('inf')]
        
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid-1
            if nums[mid-1] > nums[mid]:
                hi = mid
            else:
                lo = mid+1
        return lo-1