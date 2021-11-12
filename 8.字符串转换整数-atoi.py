#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#


# @lc code=start
class Solution:
    
    def myAtoi(self, s: str) -> int:
        class Status:
            Unknown = 0
            Positive = 1
            Negative = -1
        status = Status.Unknown
        ret, max, min = 0, 2 ** 31 - 1, -2**31
        for c in s:
            if status == Status.Unknown:
                if c == '-':
                    status = Status.Negative
                    continue
                elif c == ' ':
                    continue
                elif c == '+':
                    status = Status.Positive
                    continue
                if c.isdigit():
                    status = Status.Positive
            if not c.isdigit():
                return ret * status
            x = int(c)
            if status == Status.Positive and ret > (max - x) // 10:
                # ret * 10 + x > max
                return max
            if status == Status.Negative and ret > (-min - x) // 10:
                # -(ret * 10 + x) < min
                return min
            ret = ret * 10 + x
        return ret * status

# @lc code=end

