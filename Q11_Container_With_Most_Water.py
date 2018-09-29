class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        x_left, x_right = 0, len(height)-1
        while x_left < x_right:
            area = (x_right - x_left) * min(height[x_left], height[x_right])
            if area > max_area:
                max_area = area
            if height[x_left] < height[x_right]:
                x_left += 1
            else:
                x_right -= 1
        return max_area