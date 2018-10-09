class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return None
        r_list = []
        for num in nums:
            next_nums = nums.copy()
            next_nums.remove(num)
            deeper_l = self.permute(next_nums)
            if deeper_l:
                for l in deeper_l:
                    r_list += [[num] + l]
            else:
                r_list += [[num]]
        return r_list