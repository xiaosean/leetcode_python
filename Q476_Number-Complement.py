class Solution:
    def findComplement(self, num: int) -> int:
        fill_one_num = 2 # create n's 1 
        while fill_one_num-1 < num:
            fill_one_num <<= 1
        return (fill_one_num-1)-num