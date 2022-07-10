class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        elif len(cost) < 3:
            return min(cost)
        cost += [0]
        dp_0 = [float('inf')] * len(cost)
        dp_0[0] = cost[0]
        dp_1 = [float('inf')] * (len(cost)-1)
        dp_1[0] = cost[1]
        for i, num in enumerate(cost):
            if i-1 >= 0:
                dp_0[i] = min(dp_0[i], dp_0[i-1]+num)
            if i-2 >= 0:
                dp_0[i] = min(dp_0[i], dp_0[i-2]+num)
        for i, num in enumerate(cost[1:]):
            if i-1 >= 0:
                dp_1[i] = min(dp_1[i], dp_1[i-1]+num)
            if i-2 >= 0:
                dp_1[i] = min(dp_1[i], dp_1[i-2]+num)
        return min(dp_0[-1], dp_1[-1])
        