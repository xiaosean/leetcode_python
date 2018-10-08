class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        
        lo = 0
        hi = len(nums)-1
        while (lo <= hi):
            mid = lo + int((hi - lo) / 2);
            if target == nums[mid]:
                return mid;

#              smaller ... larger [mid] smaller ... larger             
#           rotated
            if nums[mid] < nums[lo]:
#              larger in left  find larget or rotated to right side
                if (target < nums[mid] or target >= nums[lo]):
                    hi = mid - 1;
                else:
                    lo = mid + 1;
# no rotated
            else:

                if (target > nums[mid] or target < nums[lo]):
                    lo = mid + 1;
                else:
                    hi = mid - 1;
            
        
        return -1;