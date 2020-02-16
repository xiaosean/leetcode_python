class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num+1):
            square_num = i*i
            if square_num == num:
                return True
            if square_num > num:
                break
        return False