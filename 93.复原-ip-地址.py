#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ans = []
        self.search([], s)
        return self.ans
    
    def search(self, parsed: List[str], raw: str):
        if len(parsed) == 3:
            if self.isValidSegment(raw): 
                self.ans.append('.'.join(parsed) + '.' + raw)
            return
        for i in range(1, 4):
            slice = raw[:i]
            if self.isValidSegment(slice) and self.canDivide(raw[i:], 4 - len(parsed) - 1):
                self.search([*parsed, slice], raw[i:])
    
    def isValidSegment(self, slice: str) -> bool:
        if not slice or slice != '0' and slice.startswith('0'):
            return False
        if len(slice) < 3:
            return True
        maxValue = '255'
        for i in range(3):
            if slice[i] < maxValue[i]:
                return True
            if slice[i] > maxValue[i]:
                return False
        return True
    
    def canDivide(self, raw: str, parts: int) -> bool:
        if len(raw) < parts * 1 or len(raw) > parts * 3:
            return False
        return True
        
# @lc code=end

