class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        profit_difficulty_map = sorted(zip(profit, difficulty), key=lambda x:x[0], reverse=True)
        c = Counter(worker)
        res = 0
        for k, v in sorted(c.items(), key=lambda x:x[0], reverse=True):
            while profit_difficulty_map:
                x_profit, x_difficulty = profit_difficulty_map[0]
                if k >= x_difficulty:
                    res += x_profit*v
                    break
                else:
                    del profit_difficulty_map[0]
        return res
            
