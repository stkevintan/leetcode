#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans, self.n, self.k = [], n, k
        self.tmp = []
        self.dfs(1, k)
        return self.ans
    
    def dfs(self, start: int, k: int):
        if k == 0:
            self.ans.append(self.tmp[:])
            return
        for i in range(start, self.n - k + 2):
            self.tmp.append(i)
            self.dfs(i + 1, k - 1)
            self.tmp.pop()

# @lc code=end
