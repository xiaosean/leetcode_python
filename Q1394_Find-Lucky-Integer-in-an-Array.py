from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        largest = -1
        c = Counter(arr)
        for k, v in c.items():
            if k == v:
                largest = max(largest, k)
        return largest