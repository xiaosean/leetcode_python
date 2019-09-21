class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        if not A:
            return None
        output = []
        even_sum = sum([a for a in A if a % 2 == 0 ])
        for val, index in queries:
            if A[index] % 2 == 0:
                even_sum -= A[index]
            A[index] += val
            if A[index] % 2 == 0:
                even_sum += A[index]
            output.append(even_sum)
        return output