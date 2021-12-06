from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # BFS solution
        # queue, ([], start index)
        # while queue:
        #   traverse each word
        #       if [index:index+len(word)+1] == word:
        #           push queue
        #       if index == last idx:
        #           save the res
        if not s:
            return []
        queue = deque([([], 0)])
        n = len(s)
        res = []
        while queue:
            sen, idx = queue.popleft()
            if idx == n:
                res += [" ".join(sen)]
            if idx >= n: # traverse to the end
                continue
            for word in wordDict:
                if s[idx:idx+len(word)] == word:
                    queue.append((sen + [word], idx+len(word)))
        return res
                
        