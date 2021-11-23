#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 最关键一步：
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        if x < 10:
            return True
        half, tmpX = 0, x
        while tmpX > 0:
            tmpX, c = divmod(tmpX, 10)
            half = half * 10 + c
            if half == tmpX:
                return True
            if half == tmpX // 10:
                return True
            if half > tmpX:
                return False
        
        return False

# 21120

# @lc code=end
