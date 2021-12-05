#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        rec = dict({0: 1})
        prefix, ans = 0, 0
        for x in nums:
            prefix += x
            target = prefix - k
            if target in rec:
                ans += rec[target]
            rec[prefix] = rec.get(prefix, 0) + 1

        return ans
# @lc code=end

