class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #     use extra memory
    #     s_nums = set(nums)
    #     set_2x = sum(s_nums)*2
    #     return set_2x - sum(nums)
    #     xor solution
        result = nums[0]
        for num in nums[1:]:
            result ^= num
        return result