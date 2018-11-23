class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        nums_set = list(set(nums))
        nums_dict = {num:1 for num in nums_set}
        def get_consecutive(num):
            if nums_dict[num] > 1:
                return nums_dict[num]

            consecutive_count = 1
            if num-1 in nums_dict:
                if nums_dict[num-1] > 1:
                    consecutive_count += nums_dict[num-1]
                    return consecutive_count
                consecutive_count += get_consecutive(num-1)
                nums_dict[num] = consecutive_count
                return consecutive_count
            return 1

        for num, count in nums_dict.items():
            max_count = max(max_count, get_consecutive(num))

        return max_count
