class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        r = 0
        for i in range(n):
            if r <= i:
                r = i 
                product = nums[i]
                if product < k:
                    count += 1
            else:
                count += r - i + 1
            while r < n-1:
                r += 1
                temp = product * nums[r]
                if temp < k:
                    count += 1
                    product = temp
                else:
                    r -= 1
                    break
            product /= nums[i]
        return count