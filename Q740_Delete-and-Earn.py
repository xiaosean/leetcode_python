class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnts = [0]*(max(nums)+1)
        for num in nums:
            cnts[num] += 1
        pre, cur = 0, 0
        for i in range(len(cnts)):
            pre, cur = cur, max(pre+i*cnts[i], cur)
        return cur