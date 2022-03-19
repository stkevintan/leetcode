#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
from operator import itemgetter
from typing import Callable, List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        size = len(intervals)
        lb = self.bound(lambda x: intervals[x][1], newInterval[0], size)
        rb = self.bound(lambda x: intervals[x][0], newInterval[1], size, False)
        if lb == size:
            return intervals + [newInterval]
        if rb == 0:
            return [newInterval] + intervals 
        start = min(intervals[lb][0], newInterval[0])
        end = max(intervals[rb - 1][1], newInterval[1])
        return intervals[:lb] + [[start, end]] + intervals[rb:]


    def bound(self, itemgetter: Callable[[int], int], target: int, size: int, lower: bool = True) -> int:
        l, r = 0, size
        while l < r:
            m = (l + r) >> 1
            v = itemgetter(m)
            if v > target or (lower and v == target):
                r = m
            else:
                l = m + 1
        return l

# @lc code=end

