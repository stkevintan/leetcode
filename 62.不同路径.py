#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

from math import comb
# @lc code=start


# 此题本质就是组合数学
# 区别在于计算nCr的办法：
# 1. 直接计算 n!/((n-r)!r!)
# 2. 使用公式(Pascal's triangle)：C(n,r) = C(n-1,r) + C(n-1,r-1) 因此可以衍生出递归计算，甚至是动态规划
# https://stackoverflow.com/questions/11809502/which-is-better-way-to-calculate-ncr
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 使用内置库
        # return comb(m + n - 2, m - 1)
        if m > n: 
            n, m = m, n
        return self.C(m - 1 + n - 1, m - 1)

    def C(self, n, r):
        ret = 1
        for i in range(1, r + 1):
            # 为什么这里不会除不尽呢？ 因为每一步生成的ret其实都可以写作C(n - r + i, i)
            ret = ret * (n - r + i) // i
        return ret
        
# @lc code=end

