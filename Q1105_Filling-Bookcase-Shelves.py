class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] + [float('inf')]*n
        for i in range(len(books)):
            h, w, idx = 0, 0, i
            while idx>=0 and w+books[idx][0]<=shelfWidth:
                h = max(h, books[idx][1])
                w = w+books[idx][0]
                dp[i+1] = min(dp[i+1], dp[idx]+h)
                idx -= 1
        return dp[-1]