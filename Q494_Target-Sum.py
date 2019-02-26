class Solution:
    def findTargetSumWays(self, nums: 'List[int]', S: 'int') -> 'int':
        if not nums:
            return 0
        n = len(nums)
        sum_dict = {0:1}
        for num in nums:
            temp_dict = {}
            for d in sum_dict:
                temp_dict[d + num] = temp_dict.get(d + num, 0) + sum_dict.get(d, 0)
                temp_dict[d - num] = temp_dict.get(d - num, 0) + sum_dict.get(d, 0)
            sum_dict = temp_dict
        return sum_dict.get(S, 0)