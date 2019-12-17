class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) == len(B):
            l = len(A)
            count = 0
            diff_idx = []
            for i in range(l):
                if A[i] != B[i]:
                    count += 1
                    diff_idx += [i]
                    if count > 2:
                        return False
            if count == 0 and l-len(set(A)) > 0:
                return True
            
            if count == 2:
                l_idx, r_idx = diff_idx[0], diff_idx[-1]
                if A[l_idx] == B[r_idx] and B[l_idx] == A[r_idx]:
                    return True
                
        return False