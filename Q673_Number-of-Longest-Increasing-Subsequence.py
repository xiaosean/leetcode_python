class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return None
        n = len(nums)
        dp_len = [1] * n
        dp_cnt = [1] * n
        largest = 1
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    # if dp_len[i] == dp_len[j]:
                    #     dp_len[i] = dp_len[j]+1
                    #     dp_cnt[i] = dp_cnt[j] 
                    # elif dp_len[i] == dp_len[j]+1:
                    #     dp_cnt[i] += dp_cnt[j] 
                    dp_len[i] = max(dp_len[i], dp_len[j]+1)
                    if largest < dp_len[i]:
                        largest = dp_len[i]
                        dp_cnt[i] = dp_cnt[j] 
                    elif dp_len[i] == dp_len[j]+1:
                        dp_cnt[i] += dp_cnt[j]
        return sum([dp_cnt[i] for i in range(n) if dp_len[i]==largest])
        