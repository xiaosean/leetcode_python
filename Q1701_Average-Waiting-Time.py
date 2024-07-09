class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        finish_time = 0
        res = 0
        for arr, t in customers:
            if arr > finish_time:
                finish_time = arr
            finish_time += t
            res += finish_time-arr
        return res/len(customers)