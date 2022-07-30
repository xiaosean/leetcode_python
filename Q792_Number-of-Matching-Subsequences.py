class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0
        waiting = collections.defaultdict(list)
        for word in words:
            waiting[word[0]] += [iter(word[1:])]
        for letter in s:
            for it in waiting.pop(letter, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])