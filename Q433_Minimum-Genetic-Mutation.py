from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = [(start, 0)]
        bank = set(bank)
        if len(start) != 8 or len(end) != 8 or end not in bank:
            return -1

        while queue:
            s, count = queue[0]
            del queue[0]
            for i in range(8):
                for c in "ACGT":
                    next_str = s[:i] + c + s[i+1:]
                    if next_str in bank:
                        if next_str == end:
                            return count+1
                        queue += [(next_str, count+1)]
                        bank.remove(next_str)
                    
        return -1