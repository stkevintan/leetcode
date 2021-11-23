#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.candidates, self.target, self.n = candidates, target, len(candidates)
        self.ret, self.current = [], []
        self.search(0, 0)
        return self.ret
    
    def search(self, index, sum):
        if sum == self.target:
            self.ret.append(self.current.copy()) 
            return
        if sum > self.target:
            return
        if index >= self.n:
            return
        self.current.append(self.candidates[index])
        self.search(index + 1, sum + self.candidates[index]) 
        self.current.pop()
        while index + 1 < self.n and self.candidates[index + 1] == self.candidates[index]:
            index += 1
        self.search(index + 1, sum)
    

# @lc code=end

