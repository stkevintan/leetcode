#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
from typing import Dict, List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        tmp = {}
        ret = []    
        def loop(index: int, sum: int):
            if sum == target:
                ret.append(self.interpret(tmp))
                return
            if index >= len(candidates):
                return
            i = 0
            while sum + candidates[index] * i <= target:
                tmp[candidates[index]] = i
                loop(index + 1, sum + candidates[index] * i)
                tmp[candidates[index]] = 0
                i += 1
        loop(0, 0)
        return ret
    def interpret(self, mp: Dict[int, int]):
        ret = []
        for candidate, count in mp.items():
            for _ in range(0, count):
                ret.append(candidate)
        return ret

# @lc code=end

