class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Do n times get maximum hisogram
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        
        def hist_rect_helper(nums):
            nums = [0] + nums + [0]
            stack = [0]
            area = 0
            for i in range(len(nums)):
                while len(stack) > 1 and nums[i] < nums[stack[-1]]:
                    h = nums[stack.pop()]
                    w = i-(stack[-1]+1)
                    area = max(area, h*w)
                stack += [i]
            return area
        
        histo = [0]*n       
        for y in range(m):
            for x in range(n):
                if matrix[y][x] == "1":
                    histo[x] += 1
                else:
                    histo[x] = 0
            max_area = max(max_area, hist_rect_helper(histo))
        return max_area