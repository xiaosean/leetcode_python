from collections import Counter
class Solution:
    def topKFrequent(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        c = Counter(nums)
        return [x for x, y in c.most_common(k)]