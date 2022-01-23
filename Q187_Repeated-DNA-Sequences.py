class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visit = {}
        res = []
        for i in range(len(s)-9):
            if s[i:i+10] in visit and visit[s[i:i+10]]:
                visit[s[i:i+10]] += 1
                if visit[s[i:i+10]] == 2:
                    res += [s[i:i+10]]
            else:
                visit[s[i:i+10]] = 1
        return res