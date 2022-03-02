import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        letter_dict = {}
        for letter in s:
            letter_dict[letter] = letter_dict.get(letter, 0) + 1
        heap = []
        for k, v in letter_dict.items():
            heapq.heappush(heap, (v, k))
        res = ""
        for k, v in heapq.nlargest(len(heap), heap):
            res += k*v
        return res