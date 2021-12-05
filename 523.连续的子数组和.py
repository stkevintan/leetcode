#
# @lc app=leetcode.cn id=523 lang=python3
#
# [523] 连续的子数组和
#

from typing import Dict, List
# @lc code=start


class Solution:
    # sum[i][j] = prefix[i] - prefix[j - 1] 
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        # Please note we need place a zero with -1 index as the intial value
        hash: Dict[int, int] = {0: -1}
        for i, x in enumerate(nums):
            prefix = (prefix + x) % k
            if prefix in hash: 
                if i - hash[prefix] >= 2:
                    return True
            else:
                hash[prefix] = i
        return False

# @lc code=end

