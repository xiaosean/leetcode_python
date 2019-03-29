class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        
        diff = [A[i+1] - A[i] for i in range(len(A)-1)]        
        consecutive_list = []
        last_diff = None
        last_index = 0
        count = 0
        for idx, val in enumerate(diff):
            if val != last_diff:
                if count >= 2:
                    consecutive_list += [(last_index, idx-1)]
                count = 1
                last_diff = val
                last_index = idx
            else:
                count += 1
        if count >= 2:
            consecutive_list += [(last_index, len(A)-2)]
        
        arithmetic_count = 0
        for start, end in consecutive_list:
            length = end - start + 2
            for i in range(length, 2, -1):
                arithmetic_count += length+1-i
                
        return arithmetic_count
                
        
            
            