#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
from typing import List, Set 


class Solution:
    def search(self) -> List[List[int]]:
        ret: List[List[int]] = []
        isLeast = len(self.indexTaken) + 1 == len(self.nums)
        # to prevent duplication 
        valueTaken = set()
        for i, x in enumerate(self.nums):
            if (i in self.indexTaken) or (x in valueTaken):
                continue
            if isLeast:
                return [[x]]
            valueTaken.add(x)
            self.indexTaken.add(i)
            rest = self.search()
            self.indexTaken.remove(i)
            ret.extend(map(lambda list: [x, *list], rest))
        return ret 

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.indexTaken: Set[int] = set()
        return self.search()
# @lc code=end

