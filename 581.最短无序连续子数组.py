#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# @lc code=start
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        return self.noStack(nums);

    def stack(self, nums: List[int]) -> int:
        n = len(nums)
        start = n
        stk = []
        for i in range(n): 
            while stk and nums[stk[-1]] > nums[i]:
                start = min(start, stk.pop())
            stk.append(i)
        if start == n:
            return 0
        end = -1
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and nums[stk[-1]] < nums[i]:
                end = max(end, stk.pop())
            stk.append(i)
        #print(start, end)
        return end - start + 1
    def noStack(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        right = 0
        maxN = nums[0]
        for i in range(1, n):
            if maxN > nums[i]:
                right = i
            else:
                maxN = nums[i]
        left = n - 1
        minN = nums[n - 1]
        for i in range(n - 2, -1, -1):
            if minN < nums[i]:
                left = i
            else:
                minN = nums[i]
        return right - left + 1 if right > left else 0
            


# @lc code=end

