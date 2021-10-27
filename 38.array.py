#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
from typing import List


class Solution:
    ret: List[str]
    def __init__(self) -> None:
        self.ret = ['1']
        for i in range(1, 30):
            self.ret.append(self.inferNext(self.ret[i - 1]))

    def inferNext(self, x: str) -> str:
        s = ''
        i = 0
        while i < len(x):
            j = i + 1
            while j < len(x) and x[j] == x[i]:
                j = j + 1
            s += str(j - i) + x[i]
            i = j
        return s

    def countAndSay(self, n: int) -> str:
        return self.ret[n - 1]


s = Solution()

print('\n'.join(s.ret))

# @lc code=end

