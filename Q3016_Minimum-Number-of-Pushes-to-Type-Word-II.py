class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        cnt = 0
        push = 0
        for k, v in c.most_common():
            push += v*(1+cnt//8)
            cnt+=1
        return push