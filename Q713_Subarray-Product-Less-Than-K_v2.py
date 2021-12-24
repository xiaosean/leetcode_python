class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 2 pointer solution
        # cumprod with sliding window solution
        n = len(nums)
        start = 0
        cnt = 0
        cumprod = 1
        for end in range(n):
            cumprod *= nums[end]
            while cumprod >= k and start <= end:
                cumprod //= nums[start]
                start += 1
            cnt += end-start+1
        return cnt
                
        