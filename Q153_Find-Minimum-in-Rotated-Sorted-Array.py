class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        n = len(nums)
        if n == 1:            
            return nums[0]
        if n == 2:
            return min(nums)
        l, mid, r  = nums[0], nums[n//2], nums[-1]
        if l < mid < r:
            return l
        if mid > l:
#             start~mid is ascending, we consider mid+1~end
            return self.findMin(nums[n//2+1:])
        return self.findMin(nums[:n//2+1])