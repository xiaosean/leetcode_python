class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def traverse(y, x, target):
            if 0 <= y < len(image) and 0 <= x < len(image[0]) and image[y][x] == target:
                image[y][x] = -1
                traverse(y-1, x, target)
                traverse(y+1, x, target)
                traverse(y, x-1, target)
                traverse(y, x+1, target)
                image[y][x] = newColor
        traverse(sr, sc, image[sr][sc])
        return image
                