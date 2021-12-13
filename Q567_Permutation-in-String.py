from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation means we can only calculate the count of each letters
        n = len(s1)
        s1_counter = Counter(s1)
        sub_counter = Counter(s2[:n])
        if s1_counter == sub_counter:
            return True
        for i in range(n, len(s2)):
            sub_counter[s2[i]] += 1
            sub_counter[s2[i-n]] -= 1
            if sub_counter[s2[i-n]] == 0:
                del sub_counter[s2[i-n]]
            if s1_counter == sub_counter:
                return True
        return False
            