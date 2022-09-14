class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        data = [(k, v) for k, v in c.items()]
        data = sorted(data, key= lambda x:(-x[1], x[0]))
        return [key for key, _ in data[:k]]