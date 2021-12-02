#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#

# @lc code=start
from collections import Counter
from typing import List, Set


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        inStack: Set[str] = set()
        stk: List[str] = []
        C = Counter(s)
        for c in s:
            if c in inStack:
                C[c] -= 1
                continue
            while stk:
                if stk[-1] > c and C[stk[-1]] > 1:
                    inStack.remove(stk[-1])
                    C[stk[-1]] -= 1
                    stk.pop()
                else:
                    break
            stk.append(c)
            inStack.add(c)
        return ''.join(stk)
        
# @lc code=end

