#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        x2y, y2x = {}, {}
        for i in range(len(s)):
            x, y = s[i], t[i]
            if x not in x2y:
                x2y[x] = y
            elif x2y[x] != y:
                return False
            if y not in y2x:
                y2x[y] = x
            elif y2x[y] != x:
                return False
        return True
# @lc code=end

