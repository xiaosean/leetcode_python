class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # klog(lk)
        c = collections.Counter(nums)
        res = need = 0
        for k in sorted(c):
            # print(k,c[k])
            res += c[k]*max(need-k, 0) + int(c[k]*(c[k]-1)/2)
            need = max(need, k) + c[k]
        return res