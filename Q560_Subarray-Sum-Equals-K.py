class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        last = 0
        res = 0
        for num in nums:
            last += num
            res += seen.get(last-k, 0)
            seen[last] = seen.get(last, 0) + 1
        return res