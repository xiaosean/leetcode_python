class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()

        if len(candidates) == 0:
            return []
        
        r_list = []
        for idx, num in enumerate(candidates):
            if target - num == 0:
                r_list += [[target]]
                break
            elif target - num < 0:
                break
            else:
                for l in self.combinationSum(candidates[idx:], target-num):
                    c_l = [num] + l
                    r_list += [c_l]
        return r_list
        