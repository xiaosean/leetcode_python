from collections import Counter
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hashmap_nums = {}
        pair_cnt = 0
        for idx, time_slot in enumerate(time):
            time_slot = time_slot%60
            diff = 60-time_slot if time_slot > 0 else 0
            pair_cnt += hashmap_nums.get(diff, 0)
            hashmap_nums[time_slot] = hashmap_nums.get(time_slot, 0) + 1
        return pair_cnt