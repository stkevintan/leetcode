#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return self.dpHash(nums1, nums2)
        return self.stackHash(nums1, nums2)

    def dpHash(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n2 = len(nums2)
        # dp[i] 表示第i个元素后面低几个元素刚好大于它. dp[i] = {dp[i + 1], dp[dp[i + 1]] ,....}
        dp = [-1] * n2
        map = {}
        for i in range(n2 - 1, -1, -1):
            if i != n2 - 1:
                dp[i] = i + 1
                while dp[i] != -1 and nums2[dp[i]] <= nums2[i]:
                    dp[i] = dp[dp[i]]
            map[nums2[i]] = nums2[dp[i]] if dp[i] != -1 else -1
        return [map[x] for x in nums1]

    def stackHash(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        map = {}
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            map[num] = stack[-1] if stack else -1
            stack.append(num)
        return [map[x] for x in nums1]
        

# @lc code=end
