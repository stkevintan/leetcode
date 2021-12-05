#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # return self.preprocessing(nums)
        return self.O1MemoryOnTime(nums)

    def preprocessing(nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = nums[:]
        suffix = nums[:]
        for i in range(1, n):
            prefix[i] *= prefix[i - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] *= suffix[i + 1]
        return [(prefix[i - 1] if i > 0 else 1) * (suffix[i + 1] if i + 1 < n else 1) for i in range(n)]

    def O1MemoryOnTime(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        for i in range(1, n):
            ans[i] = nums[i - 1] * ans[i - 1]
        suffix = 1
        for i in range(n - 2, -1, -1):
            suffix *= nums[i + 1]
            ans[i] *= suffix
            
        return ans


# @lc code=end
