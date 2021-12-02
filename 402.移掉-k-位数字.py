#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉 K 位数字
#

# @lc code=start
from typing import List


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk: List[str] = []
        for x in num:
            while stk:
                # 允许重复，则相等的时候不需要pop
                if stk[-1] > x and k:
                   stk.pop() 
                   k -= 1
                else:
                    break
            stk.append(x)

        while stk and k:
            stk.pop()
            k -= 1

        ans = ''.join(stk).lstrip('0')
        return ans if ans else '0'

# 注意testcase:
# 1000 1
# 9 1 
# 112 1
# @lc code=end

