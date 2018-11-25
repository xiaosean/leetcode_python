class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        money_list = []
        for idx, num in enumerate(nums):
            if idx > 1:
                money_list += [max(num + money_list[-2], money_list[-1])]
            elif idx == 1:
                money_list += [max(num, money_list[0])]
            else:
                money_list += [num]
        return money_list[-1]
        