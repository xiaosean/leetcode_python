class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        t_s = ""
        t_t = ""
        cnt = 0
        for i in range(len(s))[::-1]:
            if s[i] == '#':
                cnt += 1
            elif cnt > 0:
                cnt -= 1
                continue
            else:
                t_s += s[i]
        cnt = 0
        for i in range(len(t))[::-1]:
            if t[i] == '#':
                cnt += 1
            elif cnt > 0:
                cnt -= 1
                continue
            else:
                t_t += t[i]
        return t_s == t_t