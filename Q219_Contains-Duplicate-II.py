class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for idx, num in enumerate(nums):
            if num in d:
                if idx - d[num][-1] <= k :
                    return True
            d[num] = d.get(num, []) + [idx]
        return False
            