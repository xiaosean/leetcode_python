class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        cnt = 0
        for s in arr:
            if c[s] == 1:
                cnt += 1
                if k == cnt:
                    return s
        return ""