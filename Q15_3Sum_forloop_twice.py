class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # one solution 2 forloop with lookup table
        nums.sort()
        nums_map = {}
        for idx, num in enumerate(nums):
            nums_map[num] = nums_map.get(num, []) + [idx]
        n = len(nums)
        res = []
        for i in range(n-2):
            # avoid duplicated
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, n-1):
                if j > i+1 and nums[j] == nums[j-1]: continue
                target = 0 - nums[i] - nums[j]
                if target in nums_map and max(nums_map[target]) > j:
                    res += [[nums[i], nums[j], target]]
        return res
                    
                    