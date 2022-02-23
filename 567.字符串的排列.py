#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
from collections import deque
from typing import Counter, Deque, Dict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        A = Counter(s1)
        Q: Deque[str] = deque()
        rec = {}
        size = len(s1)
        for c in s2:
            if len(Q) == size:
                return True
            if c in A and rec.get(c, 0) < A[c]:
                Q.append(c) 
                rec[c] = rec.get(c, 0) + 1
                continue
            while Q:
                d = Q.popleft()
                rec[d] -= 1
                if d == c:
                    Q.append(c)
                    rec[c] += 1
                    break
        return len(Q) == size 
                
# @lc code=end

