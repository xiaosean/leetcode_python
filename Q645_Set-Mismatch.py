from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        n = len(nums)
        res = []
        for i in range(1, n+1):
            if c[i] == 2:
                res = [i] + res
            if c[i] == 0:
                res += [i]
            if len(res) == 2:
                return res