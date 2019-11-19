class StockSpanner:

    def __init__(self):
        self.vals = []
        self.counts = []

    def next(self, price: int) -> int:
        count = 1
        if self.vals:
            if price >= self.vals[-1]:
                count = self.counts[-1] + 1
#                 check previous points
                while count <= len(self.vals) and price >= self.vals[-count]:
                    count += self.counts[-count]
        self.vals += [price]
        self.counts += [count]
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)