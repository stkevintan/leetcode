#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i1 = len(num1) - 1
        i2 = len(num2) - 1
        ans = []
        carry = 0
        while i1 >= 0 or i2 >= 0:
            x1 = int(num1[i1]) if i1 >= 0 else 0
            x2 = int(num2[i2]) if i2 >= 0 else 0
            carry, x = divmod(carry + x1 + x2, 10)
            ans.append(str(x))
            i1 -= 1
            i2 -= 1
        ans.append(str(carry))
        ans = ''.join(reversed(ans)).lstrip('0')
        return ans if ans else '0'


# @lc code=end

