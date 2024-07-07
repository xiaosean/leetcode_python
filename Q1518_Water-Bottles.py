class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numBottles < numExchange:
            return numBottles
        return (numBottles//numExchange)*numExchange+self.numWaterBottles(numBottles//numExchange + numBottles%numExchange, numExchange)