from functools import reduce
class ProductOfNumbers:

    def __init__(self):
        self.l = []
        self.product_cache = []    
    def add(self, num: int) -> None:
        self.l += [num]
        self.product_cache += [1]
        size = len(self.l)
        if num == 0:
            self.product_cache = [0] * size
        elif num == 1:
            pass
        else:
            for i in range(size-1, -1, -1):
                if self.product_cache[i] == 0:
                    break
                self.product_cache[i] *= num
    def getProduct(self, k: int) -> int:
        return self.product_cache[-k]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)