class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        res = []
        for k in sorted(c, key=lambda x: (c[x], -x)):
            res += [k]*c[k]
        return res