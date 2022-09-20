#
# @lc app=leetcode.cn id=403 lang=python3
#
# [403] 青蛙过河
#
from typing import List

# @lc code=start


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)

        f = [[False for _ in range(n)] for _ in range(n)]

        f[0][0] = True
        for i in range(1, n):
            for j in range(0, i):
                distance = stones[i] - stones[j]
                if distance > j + 1:
                    continue
                
                f[i][distance] = f[j][distance - 1] or f[j][distance] or f[j][distance + 1]
                if i == n - 1 and f[i][distance]:
                    return True
        return False

    def canCross1(self, stones: List[int]) -> bool:
        n = len(stones)
        f = [dict() for i in range(n + 1)]
        f[1][0] = True
        for i in range(2, n + 1):
            for j in range(1, i):
                step = stones[i - 1] - stones[j - 1]
                f[i][step] = f[j].get(step, False) or (
                    step - 1 >= 0 and f[j].get(step - 1, False)) or (step + 1 < j and f[j].get(step + 1, False))
                if i == n and f[i][step]:
                    return True
        return False

# @lc code=end
