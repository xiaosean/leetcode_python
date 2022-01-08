from collections import Counter
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # sliding window with 2 variable
        longest = 0
        counter = Counter()
        l = 0
        for r in range(len(fruits)):
            counter[fruits[r]] += 1
            while len(counter) > 2:
                counter[fruits[l]] -= 1
                if counter[fruits[l]] == 0:
                    del counter[fruits[l]]
                l += 1
            longest = max(longest, r-l+1)
        return longest
                