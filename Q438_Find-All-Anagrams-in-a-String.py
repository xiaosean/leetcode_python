from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) == 0 or len(p) == 0:
            return []
        anagrams_list = []
        s_size = len(s)
        p_size = len(p)
        p_words = Counter(p)
        words = Counter(s[:p_size-1])

        for i in range(p_size-1, s_size):
            words[s[i]] += 1
            head_letter_idx = i-p_size+1
            if words == p_words:
                anagrams_list += [head_letter_idx]
            words[s[head_letter_idx]] -= 1
            if words[s[head_letter_idx]] == 0:
                del words[s[head_letter_idx]]
                
                
        return anagrams_list