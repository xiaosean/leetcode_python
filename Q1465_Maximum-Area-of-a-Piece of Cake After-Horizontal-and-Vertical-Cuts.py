class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts += [0, h]
        verticalCuts += [0, w]
        horizontalCuts.sort()
        verticalCuts.sort()
        
        longest_w = 0
        longest_h = 0
        for x, y in zip(verticalCuts[:-1], verticalCuts[1:]):
            longest_w = max(longest_w, y-x)
        for x, y in zip(horizontalCuts[:-1], horizontalCuts[1:]):
            longest_h = max(longest_h, y-x)
        return longest_w*longest_h%(10**9 + 7)