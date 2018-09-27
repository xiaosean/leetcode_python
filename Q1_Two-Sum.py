class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        r_list = []
        print(nums)
        num_hash = {}
        for id1, num1 in enumerate(nums):
            num_hash[str(num1)] = id1
         
        for it in range(len(nums)):
            complement = target - nums[it]
            complement_id = num_hash.get(str(complement), -1)
            if complement_id != -1 and it != complement_id:
                r_list = [it, complement_id]
                break
        return r_list