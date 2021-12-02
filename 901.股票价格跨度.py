#
# @lc app=leetcode.cn id=901 lang=python3
#
# [901] 股票价格跨度
#

# @lc code=start
from typing import List, Tuple


class StockSpanner:

    def __init__(self):
        self.stk: List[Tuple[int, int]] = []
        self.last = 0

    def next(self, price: int) -> int:
        while self.stk:
            if self.stk[-1][1] <= price:
                self.stk.pop()
            else:
                break
        if self.stk:
            ans = self.last - self.stk[-1][0]
        else:
            ans = self.last + 1
        self.stk.append((self.last, price))
        self.last += 1
        return ans



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

