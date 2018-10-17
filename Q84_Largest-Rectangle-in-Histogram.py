class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            # if smaller than last, this is new bottleneck
            # 4 5 last=>6 3<=current
            # 4 last=>5 6 3<=current
            # last=>4 5 6 3<=current
            while heights[i] < heights[stack[-1]]:
    #             take last stack 4
                h = heights[stack.pop()]
    #             last bottleneck and this new bottleneck
    #             first take 6 | 4 stack[-1]=>5 6(pop) 3 <= i
    #             first take 5 | stack[-1]=>4 5(pop) 6 3 <= i
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans