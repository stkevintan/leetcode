#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

from typing import List
# @lc code=start


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for i in range(0, n):
            for j in range(0, m):
                if i > 0 and j == 0:
                    grid[i][j] += grid[i - 1][j]
                elif i == 0 and j > 0:
                    grid[i][j] += grid[i][j-1]
                elif i > 0 and j > 0:
                    grid[i][j] += min(grid[i][j-1], grid[i - 1][j])
        return grid[-1][-1]
# @lc code=end
