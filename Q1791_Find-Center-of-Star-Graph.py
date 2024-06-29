class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        weights = [0]*(len(edges)+2)
        for x, y in edges:
            weights[x] += 1
            weights[y] += 1
        return weights.index(len(edges))