#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for i in range(1 << n):
            tmp = []
            for k in range(n):
                if (1 << k) & i:
                    tmp.append(nums[k])
            ans.append(tmp)
        return ans

# @lc code=end

