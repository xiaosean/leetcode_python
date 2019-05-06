class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n = len(S)
        out = [n for _ in range(len(S))]
        c_map = []
        for idx, c in enumerate(S):
            if c == C:
                c_map += [idx]
                out[idx] = 0
        for idx, c in enumerate(S):
            if out[idx] == 0:
                continue
            out[idx] = min([abs(idx-x) for x in c_map])
        return out 
