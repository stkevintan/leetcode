#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
from typing import Counter, List, Tuple


# 0/1 pack
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for word in strs:
            cn, cm = self.count(word)
            for i in range(n, cn - 1, -1):
                for j in range(m, cm - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - cn][j - cm] + 1)
        
        return dp[n][m]
    
    def count(self, word: str) -> Tuple[int, int]:
        c = Counter(word)
        return c.get('1', 0), c.get('0', 0)
        
# @lc code=end

