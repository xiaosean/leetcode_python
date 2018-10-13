from collections import Counter
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n = len(s)
        start = end = 0
        dict_t = Counter(t)
        missing = sum(dict_t.values())
        dict_s = {}
        min_distance, substring = n+1, ""
        while end < n:
            letter = s[end]
            if letter in dict_t:
                dict_t[letter] -= 1
                missing -= dict_t[letter] >= 0
            if missing == 0:
                while missing == 0:
                    front_letter = s[start]
                    while front_letter not in dict_t:
                        start += 1
                        front_letter = s[start]
                    dict_t[front_letter] += 1
                    missing += dict_t[front_letter] > 0
        #                 missing still zero need to find next letter
                    start += missing == 0
                if end - start + 1 < min_distance:
                    min_distance = end - start + 1
                    substring = s[start:end+1]
                start += 1
            end += 1
        return substring