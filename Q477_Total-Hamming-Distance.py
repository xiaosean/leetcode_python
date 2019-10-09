class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        bin_nums = [bin(num)[2:] for num in nums]
        max_len = max([len(str_bin) for str_bin in bin_nums])
        bin_nums = [str_bin.zfill(max_len) for str_bin in bin_nums]
        n = len(bin_nums)
        print(bin_nums)
        diff = zeros = ones = 0
        for i in range(max_len):
            zeros = ones = 0
            for digit in bin_nums:
                if digit[i] == '1':
                    ones += 1
                else:
                    zeros += 1
            diff += ones*zeros
    return diff
        