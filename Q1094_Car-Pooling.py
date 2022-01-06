class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # reform find the intersection interval
        dp = [0] * 1001
        for trip in trips:
            num, from_, to_ = trip
            for i in range(from_, to_):
                dp[i] += num
                if dp[i] > capacity:
                    return False
        return True