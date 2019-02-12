class Solution:
    def subarraySum(self, nums: 'List[int]', k: 'int') -> 'int':
        n = len(nums)
        if n == 0:
            return 0
        count = {0:1}
        pre_sum = res = 0
        for num in nums:
            pre_sum += num
            res += count.get(pre_sum - k, 0)
            count[pre_sum] = count.get(pre_sum, 0) + 1
        return res