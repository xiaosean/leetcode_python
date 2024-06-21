class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        sliding_window = 0
        secret = 0
        sum_ = 0 
        for i, (customer, select) in enumerate(zip(customers, grumpy)):
            sum_ += customer*(1-select)
            sliding_window += customer*(select)
            if i >= minutes:
                sliding_window -= customers[i-minutes]*(grumpy[i-minutes])
            secret = max(secret, sliding_window)
        return sum_+secret
