class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(map(int, str(num))) 
        n = len(nums)
        for index, num_ in enumerate(nums[:-1]):
            max_num = max(nums[index+1:])
            if num_ < max_num:
                for e_id in range(n-1, index, -1):
                    e_num = nums[e_id]
                    if e_num == max_num:
                        nums[index], nums[e_id] = e_num, num_
                        return int("".join(list(map(str, nums))))
                
        return num