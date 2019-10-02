class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1], [1, 1]]
        if numRows == 0:
            return []
        if numRows > len(pascal):
            for height in range(1, numRows):
                row = [1]
                cur = 1
                for item in pascal[-1][1:]:
                    last, cur = cur, item
                    row += [last + cur]
                row += [1]
                pascal += [row]
        return pascal[:numRows]
            
            