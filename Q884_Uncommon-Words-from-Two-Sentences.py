from collections import Counter
from itertools import chain
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        counter_sen = Counter(chain(A.split(), B.split()))
        uncommon_words = []
        for key, value in counter_sen.items():
            if value == 1:
                uncommon_words += [key]
        return uncommon_words