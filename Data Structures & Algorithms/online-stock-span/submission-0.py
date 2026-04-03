class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 0
        self.stack.append(price)
        last = len(self.stack) - 1
        while last >= 0 and price >= self.stack[last]:
            count += 1
            last -= 1
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)