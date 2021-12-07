from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        bfs solution: 
        queue: [(0, step) for step in nums[0]]
        
        cnt = 0
        while queue:
            cnt += 1
            for idx, step in queue:
                if idx + step == last_idx:
                    return cnt
                queue.append([(idx+step, new_step) for new_step in nums[idx+step]])
        """
        if len(nums) == 1:
            return 0
        cur_list, next_list = [0], []
        cnt = 0
        traverse_map = [False] * len(nums)
        while cur_list:
            cnt += 1
            for pos in cur_list:
                if traverse_map[pos]:
                    continue
                traverse_map[pos] = True
                for next_step in range(1, nums[pos]+1)[::-1]:
                    next_pos = pos+next_step
                    if next_pos >= len(nums) - 1:
                        return cnt
                    next_list += [next_pos]
            cur_list, next_list = next_list, []
            
                
        return 0