#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

from functools import cmp_to_key
# @lc code=start
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = sorted(map(lambda x: str(x), nums), key=cmp_to_key(self.cmp))
        ans = ''.join(strs).lstrip('0')
        return ans if ans else '0'
    
    def cmp(self, x: str, y: str)-> int:
        return -1 if x + y >= y + x  else 1
    
# @lc code=end

