class ProductOfNumbers:

    # def __init__(self):
    #     self.prefix_prod = []
    #     self.last_zero_seen = -1

    # def add(self, num: int) -> None:
    #     if num == 0:
    #         self.last_zero_seen = len(self.prefix_prod)
    #         self.prefix_prod.append(num)
    #         return
    #     if not self.prefix_prod:
    #         self.prefix_prod.append(num)
    #         return

    #     self.prefix_prod.append(num * max(1, self.prefix_prod[-1]))

    # def getProduct(self, k: int) -> int:
        
    #     if self.last_zero_seen != -1 and (len(self.prefix_prod) - k) <= self.last_zero_seen:
    #         return 0
    #     return self.prefix_prod[-1] if k == len(self.prefix_prod) else self.prefix_prod[-1] // max(1, self.prefix_prod[-1-k])


    def __init__(self):
        self.data = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.data = [1]
        else:
            self.data.append(self.data[-1] * num)


    def getProduct(self, k: int) -> int:
        if k > len(self.data) - 1:
            return 0
        else:
            return self.data[-1] // self.data[-1-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)