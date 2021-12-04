#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
# count of factor 2 must be greater than factor 5, so we just find the count of factor 5
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            n = n // 5
            ans += n
        return ans
# @lc code=end

