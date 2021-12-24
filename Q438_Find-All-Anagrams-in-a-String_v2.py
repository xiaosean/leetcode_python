class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_map = [0] * 26
        target_map = [0] * 26
        for letter in p:
            target_map[ord(letter)-ord("a")] += 1
        res = []
        for idx, letter in enumerate(s):
            count_map[ord(letter)-ord("a")] += 1
            if idx >= len(p):
                count_map[ord(s[idx-len(p)])-ord("a")] -= 1
            if idx >= len(p)-1:
                equal_flag = True
                for i in range(26):
                    if count_map[i] != target_map[i]:
                        equal_flag = False
                        break
                if equal_flag:
                    res += [idx-len(p)+1]
        return res