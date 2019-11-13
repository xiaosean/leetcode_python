class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums:
            return None
        n = len(nums)
        pre_k_num = 0
        max_subary_avg = sum(nums[:k])/k
        accm_num = 0
        dp_ = [0]
        for i, num in enumerate(nums):
            avg_num = num / k
            accm_num += avg_num
            dp_ += [avg_num]
            if i >= k-1:
                accm_num -= dp_[i+1-k]
                max_subary_avg = max(max_subary_avg, accm_num)
                
        return max_subary_avg
        