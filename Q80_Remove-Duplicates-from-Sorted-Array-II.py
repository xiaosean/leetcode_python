class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_num = None
        count = 0
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            if last_num == num:
                count += 1
                if count > 2:
                    del nums[i]
            else:
                count = 1
                last_num = num