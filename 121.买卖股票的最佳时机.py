#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

from typing import List
# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smalleast = -1
        ans = 0
        for price in prices:
            if smalleast == -1 or smalleast > price:
                smalleast = price
            else:
                ans = max(ans, price - smalleast)
        return ans
# @lc code=end

