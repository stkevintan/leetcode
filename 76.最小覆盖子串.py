#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
from collections import Counter
from typing import Tuple


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        self.s, self.cnt = s, Counter(t)
        ans = ""
        self.jump = [i for i in range(len(s)) if s[i] in self.cnt]
        i, k, self.remain = 0, 0, len(self.cnt)
        while i < len(self.jump):
            start, end = self.capture(i, k)
            if start < 0:
                break
            if len(ans) == 0 or len(ans) > self.jump[end] - self.jump[start] + 1:
                ans = s[self.jump[start]:self.jump[end] + 1]
            i, k= start + 1, end + 1

        return ans

    def capture(self, i: int, k: int) -> Tuple[int, int]:
        for j in range(k, len(self.jump)):
            c = self.s[self.jump[j]]
            self.cnt[c] -= 1
            if self.cnt[c] == 0:
                self.remain -= 1
            if self.remain == 0:
                # release the left most
                while i < j:
                    shift = self.s[self.jump[i]]
                    self.cnt[shift] += 1
                    if self.cnt[shift] > 0:
                        self.remain += 1
                        break
                    i += 1
                return (i, j)
        return (-1, -1)


# @lc code=end
