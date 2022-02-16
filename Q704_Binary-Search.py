class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l+r)//2
            num = nums[mid]
            if num == target:
                return mid
            elif num < target:
                l = mid+1
            else:
                r = mid
        return -1