class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def traverse(i, j, last_val,arr):
            if i < 0 or i >= h or j < 0 or j >= w or heights[i][j] < last_val or arr[i][j]:
                return arr
            arr[i][j] = 1
            for shift_y, shift_x in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                traverse(i+shift_y, j+shift_x, heights[i][j], arr)
            return arr
        
        h, w = len(heights), len(heights[0])
        # res = [(0, 0), (h-1, w-1)]
        left = [[i, 0] for i in range(h)]
        top = [[0, i] for i in range(1, w)]
        right = [[i, w-1] for i in range(h)]
        bottom = [[h-1, i] for i in range(0, w-1)]
        
        arr1 = [[0]*w for _ in range(h)]
        for i, j in left + top:
            traverse(i, j, -1, arr1)
        arr2 = [[0]*w for _ in range(h)]
        for i, j in right + bottom:
            traverse(i, j, -1, arr2)
        res = []
        for i in range(h):
            for j in range(w):
                if arr1[i][j] and arr2[i][j]:
                    res += [(i, j)]
        return res