from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        char_table = Counter(S)
        if not char_table:
            return ""
        most_common_char, most_common_val = char_table.most_common(1)[0]
        else_sum_val = len(S) - most_common_val
        if else_sum_val < most_common_val-1:
            return ""
        res = most_common_char
        most_common_val -= 1
        char_table[most_common_char] = 0
        while any(char_table.values()):
            c, _ = char_table.most_common()[0]
            char_table[c] -= 1
            res += c
            if most_common_val > 0:
                most_common_val -= 1
                res += most_common_char
        return res
        
            