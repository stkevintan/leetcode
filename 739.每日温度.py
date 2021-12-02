#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

from typing import List
# @lc code=start


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            while len(stack) > 0 and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            ans[i] = stack[-1] - i if len(stack) > 0 else 0
            stack.append(i)
        return ans
# @lc code=end

