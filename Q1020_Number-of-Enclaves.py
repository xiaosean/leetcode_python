class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        def traverse_4_direction(nums, r, c):
            r_size = len(nums)
            c_size = len(nums[0])
            cells_pos = []
            if r > 0:
                cells_pos += [(r-1, c)]
            if r < r_size-1:
                cells_pos += [(r+1, c)]
            if c > 0:
                cells_pos += [(r, c-1)]
            if c < c_size-1:
                cells_pos += [(r, c+1)]
            for x, y in cells_pos:
                if nums[x][y] == 1:
                    nums[x][y] = 2
                    traverse_4_direction(nums, x, y)
        
        if not A or not A[0]:
            return None
        
        r_size = len(A)    
        c_size = len(A[0])
        for x in range(r_size):
            for y in [0, c_size-1]:
                if A[x][y] == 1:
                    A[x][y] = 2
                    traverse_4_direction(A, x, y)
        for x in [0, r_size-1]:
            for y in range(c_size):
                if A[x][y] == 1:
                    A[x][y] = 2
                    traverse_4_direction(A, x, y)
        enclaves = 0
        for x in range(r_size):
            for y in range(c_size):
                if A[x][y] == 1:
                    enclaves += 1 
        return enclaves
            
                    