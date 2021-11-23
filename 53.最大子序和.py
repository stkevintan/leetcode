#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

from enum import Enum
from typing import List
# @lc code=start


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maxSum = nums[0]
#         curSum = nums[0]
#         for i in range(1, len(nums)):
#             # curSum + nums[i] > nums[i]
#             if curSum > 0:
#                 curSum += nums[i]
#             else:
#                 curSum = nums[i]
#             maxSum = max(maxSum, curSum)
#         return maxSum


# 线段树
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        class Node:
            def __init__(self, sum=0, rMaxSum=0, lMaxSum=0, maxSum=0) -> None:
                # total sum
                self.sum = sum
                # max sum ends with right-most element
                self.rMaxSum = rMaxSum
                # max sum starts with left-most element
                self.lMaxSum = lMaxSum
                # max sum overall
                self.maxSum = maxSum

        class Solve:
            def pushUp(self, left: Node, right: Node) -> Node:
                ret = Node(
                    sum=left.sum + right.sum,
                    lMaxSum=max(left.lMaxSum, left.sum + right.lMaxSum),
                    rMaxSum=max(right.rMaxSum, right.sum + left.rMaxSum)
                )
                ret.maxSum = max(ret.lMaxSum, ret.rMaxSum,
                                 left.maxSum, right.maxSum,
                                 left.rMaxSum + right.lMaxSum)
                return ret

            def build(self, L: int, R: int) -> Node:
                if L == R:
                    return Node(nums[L], nums[L], nums[L], nums[L])
                M = (L + R) >> 1
                left = self.build(L, M)
                right = self.build(M + 1, R)
                # push up
                return self.pushUp(left, right)
        solver = Solve()
        return solver.build(0, len(nums) - 1).maxSum


# @lc code=end
