class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        min_cnt = n + 1
        
        for target in range(1, 7):
            top_cnt = 0
            bottom_cnt = 0
            for idx in range(n):
                top, bottom = tops[idx], bottoms[idx]
                if top != target and bottom != target:
                    break
                elif top == target and bottom != target:
                    bottom_cnt += 1
                elif top != target and bottom == target:
                    top_cnt += 1
                
                if idx == n-1:
                    min_cnt = min(min_cnt, top_cnt, bottom_cnt)
        return min_cnt if min_cnt < n else -1