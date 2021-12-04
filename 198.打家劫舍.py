#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        return self.rob2(nums)
    
    def rob0(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = [0] * n # max cash when take i room
        dp2 = [0] * n # max cash when don't take i room
        for i, x in enumerate(nums):
            if i == 0:
                dp1[i] = x
                dp2[i] = 0
            else:
                dp1[i] = dp2[i - 1] + x
                dp2[i] = max(dp1[i - 1], dp2[i - 1])
        return max(dp1[n - 1], dp2[n - 1])

    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i, x in enumerate(nums):
            if i == 0:
                dp[i] = x
            elif i == 1:
                dp [i] = max(dp[i - 1], dp[i])
            else:
                dp[i] = max(dp[i - 2] + x, dp[i - 1])
        return dp[i]
    
    def rob2(self, nums: List[int]) -> int:
        n = len(nums)
        if n in self.memo:
            return self.memo[n]
        ans = 0
        if 0 < n < 2:
            ans = max(nums)
        elif n >= 2:
            ans = max(self.rob2(nums[:-1]), self.rob2(nums[:-2]) + nums[-1])
        self.memo[n] = ans
        return ans

# @lc code=end

