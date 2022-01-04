class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = [0]
        max_area = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i-stack[-1]-1
                max_area = max(max_area, w*h)    
            stack += [i]
            
        return max_area