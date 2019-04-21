class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        s = [i for i in range(len(S)+1)]
        match_s = []
        pre = ""
        count = 0
        S += " "
        
        for i in range(len(S)):
            if S[i] == pre:
                count += 1
            else:
                if pre == "I":
                    match_s += [letter for letter in s[:count]]
                    s = s[count:]
                elif pre == "D":
                    match_s += [letter for letter in s[len(s)-count:][::-1]]
                    s = s[:len(s)-count]
                count = 1
                pre = S[i]
        match_s += s
        
        return match_s