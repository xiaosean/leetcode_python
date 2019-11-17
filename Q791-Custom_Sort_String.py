import heapq
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        s_size = len(S)
        mapping_table = {S[i]: s_size-i for i in range(s_size)}
        t_size = len(T)
        heap = []
        for idx in range(t_size):
            letter = T[idx]
            heapq.heappush(heap, (mapping_table.get(letter, -1), letter))
        res = [letter for _, letter in heapq.nlargest(t_size, heap)]
        return "".join(res)