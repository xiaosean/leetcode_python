class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (lo+hi)//2
            if nums[hi] == target or nums[lo] == target or nums[mid] == target:
                return True
            # check if rotated:
            if nums[lo] == nums[hi]:
                lo += 1
                hi -= 1  
            elif nums[mid] == nums[hi]:
                hi = mid-1
            elif nums[mid] == nums[lo]:
                lo = mid+1
            elif (nums[mid]-nums[hi]) * (target-nums[hi]) > 0:
                if target > nums[mid]:
                    lo = mid+1
                else:
                    hi = mid
            elif target > nums[hi]:
                hi = mid
            else:
                lo = mid+1
        return nums[lo]==target