class Solution:
    
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sum_ = sum([cost[0] for cost in costs])
        diff = [cost2-cost1 for cost1, cost2 in costs]
        diff.sort()
        for i in range(len(costs)//2):
            sum_ += diff[i]
        return sum_