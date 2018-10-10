class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        jump_table = {}

        def deepJump(idx):
    #         if have already jumping
            if jump_table.get(str(idx), False) == False:
                jump_table[str(idx)] = True
            else:
                return False

            num = nums[idx]
    #         print("num = %d idx = %d final_index = %d" % (num, idx, final_index))
            if num + idx >= final_index:
                return True
    # if maximum jumping already search
            if jump_table.get(num + idx, False):
                return False
    # start recursive search
            for i in range(num, 0, -1):
                if deepJump(idx+i):
                    return True
            return False    


        final_index = len(nums)-1
        if final_index == 0:
            return True
    #     trace possible or not
        possible_flag = False
        for idx, num in enumerate(nums[:-1]):
            if idx + num >= final_index:
                possible_flag = True
                break

        if possible_flag:
            return deepJump(0)
        else:
            return False
