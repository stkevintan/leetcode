#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

from typing import List

# @lc code=start


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sz = len(gas)
        diff = [gas[i] - c for (i, c) in enumerate(cost)] * 2
        sum, count = 0, 0
        for i in range(len(diff) - 1):
            sum += diff[i]
            count += 1
            if sum < 0:
                sum = count = 0
            elif count == sz:
                return i - count + 1
        return -1



# @lc code=end
