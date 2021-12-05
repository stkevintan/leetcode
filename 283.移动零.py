#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        return self.swap(nums)

    # for case 000001, it which need operate 6 times. but actually we only need swap the two endpoints.
    def cover(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        for x in nums:
            if x != 0:
                nums[p] = x
                p += 1
        for i in range(p, len(nums)):
            nums[i] = 0
        return nums
    
    def swap(self, nums: List[int]) -> None:
        slowptr, fastptr, n = 0, 0, len(nums)
        while fastptr < n:
            if nums[fastptr]:
                if slowptr != fastptr:
                    nums[slowptr], nums[fastptr] = nums[fastptr], nums[slowptr]
                slowptr += 1
            fastptr += 1
    
            
# @lc code=end

