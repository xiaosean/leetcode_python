class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if not A:
            return None
        odd_idices = []
        even_idices = []
        for idx, item in enumerate(A):
            if item % 2 == 0:
                even_idices += [idx]
            else:
                odd_idices += [idx]
        
        return [A[idx] for idx in even_idices] + [A[idx] for idx in odd_idices]